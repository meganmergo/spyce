import sys
import math

import vector
import gui.textures
import gui.skybox
import gui.picking
import gui.terminal
from gui.graphics import *


class SystemGUI(gui.picking.PickingGUI, gui.terminal.TerminalGUI):
    """GUI for showing a planetary system"""
    def __init__(self, focus):
        title = b'Sp' + b'a'*42 + b'ce'
        super(SystemGUI, self).__init__(title)

        self.time = 0
        self.zoom = 1e-7

        # detect current system
        self.focus = focus
        self.system = self.focus
        while self.system.orbit is not None:
            self.system = self.system.orbit.primary

        glEnable(GL_POINT_SPRITE)
        self.shader_position_marker = main_program(None, "circle_point.frag")

        # sphere VBO for drawing bodies
        n = 64
        self.sphere_vertices = BufferObject(sphere(n, n), flatten=True)
        self.sphere_texcoords = BufferObject(sphere_tex(n, n), flatten=True)

        # VBOs for drawing orbits

        # unit circle centered on (0, 0)
        n = 512
        vertices = []
        for i in range(n):
            x = 2.*i/(n-1) - 1  # from -1.0 to +1.0
            theta = math.pi * x
            vertices += [math.cos(theta), math.sin(theta), 0.]
        self.circle = BufferObject(vertices)

        # unit circle centered on (1, 0)
        n = 256
        vertices = []
        for i in range(n):
            x = 2.*i/(n-1) - 1  # from -1.0 to +1.0
            theta = math.pi * x**3
            vertices += [1. - math.cos(theta), math.sin(theta), 0.]
        self.shifted_circle = BufferObject(vertices)

        # unit parabola centered on (0, 0)
        n = 256
        vertices = []
        for i in range(n):
            x = 2.*i/(n-1) - 1  # from -1.0 to +1.0
            theta = math.pi * x
            vertices += [math.cosh(theta), math.sinh(theta), 0.]
        self.parabola = BufferObject(vertices)

        # make call lists for orbits
        def make_orbit_call_list(body):
            if body.orbit:
                body.orbit.call_list = glGenLists(1)
                glNewList(body.orbit.call_list, GL_COMPILE)
                self.draw_orbit(body.orbit)
                glEndList()
            for satellite in body.satellites:
                make_orbit_call_list(satellite)
        make_orbit_call_list(self.system)

        # textures
        gui.textures.init()
        texture_directory = self.system._texture_directory

        def load_body(body):
            """Recursively load textures for celestial bodies"""
            filename = "%s.jpg" % body.name
            body.texture = gui.textures.load(texture_directory, filename)
            for satellite in body.satellites:
                load_body(satellite)
        load_body(self.system)

        # skybox
        self.skybox = gui.skybox.Skybox("skybox", "GalaxyTex_%s.jpg")

    @classmethod
    def from_cli_args(cls):
        """Load the system given in command-line arguments"""
        import load

        try:
            name = sys.argv[1]
        except IndexError:
            name = 'Kerbin'

        try:
            body = load.from_name(name)
        except KeyError:
            sys.stderr.write("Unknwon body '%s'\n" % name)
            sys.exit(1)

        return cls(body)

    def draw_orbit(self, orbit):
        """Draw an orbit using focus as origin"""
        glPushMatrix()

        # make tilted ellipse from a circle or tilted hyperbola from a parabola
        glRotatef(math.degrees(orbit.longitude_of_ascending_node), 0, 0, 1)
        glRotatef(math.degrees(orbit.inclination),                 1, 0, 0)
        glRotatef(math.degrees(orbit.argument_of_periapsis),       0, 0, 1)
        glTranslatef(-orbit.focus, 0, 0)
        glScalef(orbit.semi_major_axis, orbit.semi_minor_axis, 1.0)

        # draw circle or parabola
        if orbit.eccentricity < 1.:
            self.circle.draw(GL_LINE_STRIP)
        else:
            self.parabola.draw(GL_LINE_STRIP)

        # apses
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex3f(+1, 0, 0)
        if orbit.eccentricity < 1.:
            glVertex3f(-1, 0, 0)
        glEnd()

        glPopMatrix()

    def draw_orbit_focused(self, body):
        """Draw on orbit using current position as origin"""

        # issues when drawing the orbit a focused body:
        # 1. moving to system center and back close to camera induces
        #    loss of significance and produces jitter
        # 2. drawing the orbit as segments may put the body visibly out
        #    of the line when zooming in
        # 3. line breaks may be visible close to the camera

        # now, we fix the three issues mentioned above
        # draw the orbit from the body rather than from the orbit focus (1.)

        def corrected_orbit_position(theta):
            return body.orbit.position(theta) - focus_offset
        focus_offset = body.orbit.position_t(self.time)

        orbit = body.orbit

        if orbit.eccentricity >= 1.:
            # path
            glBegin(GL_LINE_STRIP)
            n = 128
            # ensure the body will be on the line (2.)
            x = orbit.true_anomaly(self.time)
            for i in range(n):
                # we need more points close to the camera (3.)
                # the function i -> 2.*i/n - 1
                # has values in [-1, 1] and a lower slope around 0
                theta = x + math.pi * (2.*i/n - 1)**3
                relative_p = corrected_orbit_position(theta)
                glVertex3f(*relative_p)
            glEnd()

            # apses
            glPointSize(5)
            glBegin(GL_POINTS)
            glVertex3f(*corrected_orbit_position(0))
            glEnd()
        else:
            # nice hack with circle symetry to draw the orbit from the body
            # while still using VBOs
            # unsure it can be adapted for parabolic and hyperbolic orbits

            glPushMatrix()

            # the first point of shifted_circle is (0,0) (2.)
            # using linear transforms spreads points more naturally (3.)

            # make tilted ellipse from a circle
            glRotatef(math.degrees(orbit.longitude_of_ascending_node), 0, 0, 1)
            glRotatef(math.degrees(orbit.inclination),                 1, 0, 0)
            glRotatef(math.degrees(orbit.argument_of_periapsis),       0, 0, 1)
            glScalef(orbit.semi_major_axis, orbit.semi_minor_axis, 1.0)

            # account for current position of the body (use circle symmetry)
            anomaly = orbit.eccentric_anomaly(self.time)
            glRotatef(math.degrees(anomaly) - 180., 0, 0, 1)

            self.shifted_circle.draw(GL_LINE_STRIP)

            glPopMatrix()

            # apses
            glPointSize(5)
            glBegin(GL_POINTS)
            glVertex3f(*corrected_orbit_position(0))
            glVertex3f(*corrected_orbit_position(math.pi))
            glEnd()

    def draw_sphere(self, radius):
        """Draw a sphere of given radius"""
        glPushMatrix()
        glScalef(radius, radius, radius)
        self.sphere_vertices.draw(GL_QUAD_STRIP, self.sphere_texcoords)
        glPopMatrix()

    def draw_body(self, body):
        """Draw a CelestialBody"""

        glPushMatrix()
        # OpenGL use single precision while Python has double precision
        # reducing modulo 2 PI in Python reduces loss of significance
        turn_fraction, _ = math.modf(self.time / body.rotational_period)
        glRotatef(360. * turn_fraction, 0, 0, 1)

        # textured quadric (representation from close by)
        # sphere with radius proportional to that of the body
        gui.textures.bind(body.texture, (0.5, 0.5, 1.0))
        self.draw_sphere(body.radius)
        gui.textures.unbind()

        glPopMatrix()

        glDepthMask(True)

    def draw_satellites(self, body, skip=None, max_depth=None):
        """Recursively draw the satellites of a body"""
        if max_depth is not None:
            if max_depth == 0:
                return
            max_depth -= 1

        for satellite in body.satellites:
            if satellite != skip:
                self.add_pick_object(satellite)
                glPushMatrix()
                glColor4f(1.0, 1.0, 0.0, 0.2)
                if hasattr(satellite.orbit, "call_list"):
                    glCallList(satellite.orbit.call_list)
                else:
                    self.draw_orbit(satellite.orbit)
                glTranslatef(*satellite.orbit.position_t(self.time))
                self.draw_body(satellite)
                self.draw_satellites(satellite, body, max_depth)
                glPopMatrix()

    def draw_system(self, body, skip=None):
        """Draw the whole system a body belongs to"""
        self.add_pick_object(body)
        self.draw_body(body)

        self.draw_satellites(body, skip, 1)

        # recursively draw primary
        if body.orbit is not None:
            glPushMatrix()
            glColor4f(1.0, 1.0, 0.0, 1.0)
            self.draw_orbit_focused(body)
            glTranslatef(*-body.orbit.position_t(self.time))
            self.draw_system(body.orbit.primary, body)
            glPopMatrix()

    def draw_satellite_points(self, body, offset, skip=None, max_depth=None):
        """Recursively draw the satellites of a body as points"""
        if max_depth is not None:
            if max_depth == 0:
                return
            max_depth -= 1

        for satellite in body.satellites:
            if satellite == skip:
                continue

            self.add_pick_object(satellite, GL_POINTS)
            new_offset = offset + satellite.orbit.position_t(self.time)
            glVertex3f(*new_offset)
            self.draw_satellite_points(satellite, new_offset, body, max_depth)

    def draw_system_points(self, body, offset, skip=None):
        """Draw the whole system as points"""
        self.draw_satellite_points(body, offset, skip, 1)

        self.add_pick_object(body, GL_POINTS)
        glVertex3f(*offset)

        # recursively draw primary
        if body.orbit is not None:
            new_offset = offset - body.orbit.position_t(self.time)
            self.draw_system_points(body.orbit.primary, new_offset, body)

    def draw(self):
        """Draw the scene"""
        self.draw_system(self.focus)

        # point (representation from far away)
        # draw spheres of constant visible radius at body positions
        glPointSize(20)
        glDepthMask(False)
        self.shader_set(self.shader_position_marker)
        glBegin(GL_POINTS)
        glColor4f(1, 0, 0, 0.5)
        self.draw_system_points(self.focus, vector.Vector([0, 0, 0]))
        glEnd()
        self.shader_reset()
        glDepthMask(True)

    def set_and_draw(self):
        """Setup the camera and draw"""

        # reset everything
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.pick_reset()

        # skybox
        glLoadIdentity()
        glRotatef(self.phi,   1, 0, 0)
        glRotatef(self.theta, 0, 0, 1)
        glDisable(GL_DEPTH_TEST)
        self.skybox.draw()
        glEnable(GL_DEPTH_TEST)

        # set up camera
        glLoadIdentity()
        glTranslatef(0, 0, -1/self.zoom)
        glRotatef(self.phi,   1, 0, 0)
        glRotatef(self.theta, 0, 0, 1)

        self.draw()
        self.pick_clear()

    def draw_hud(self):
        """Draw the HUD"""
        self.hud_print("Focus: %s\n" % self.focus)
        super(SystemGUI, self).draw_hud()

    @glut_callback
    def mouseFunc(self, button, state, x, y):
        """Handle mouse clicks (GLUT callback)"""
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            # body selection
            self.focus = self.pick(x, y, self.focus)
            self.update()
        else:
            super(SystemGUI, self).mouseFunc(button, state, x, y)

if __name__ == '__main__':
    SystemGUI.from_cli_args().main()
