from manim import *
import numpy as np

class SineWaveAnimation(Scene):
    def construct(self):

        axes = Axes(
            x_range=[-2*np.pi, 2*np.pi, np.pi/2],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
            x_length=10,
            y_length=4,
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        amplitude = ValueTracker(1)
        phase = ValueTracker(0)

        graph = always_redraw(
            lambda: axes.plot(
                lambda x: amplitude.get_value() * np.sin(x + phase.get_value()),
                x_range=[-2*np.pi, 2*np.pi],
                color=YELLOW
            )
        )

        equation = always_redraw(
            lambda: MathTex(
                r"y = {:.1f}\sin(x + {:.1f})".format(
                    amplitude.get_value(),
                    phase.get_value()
                )
            ).to_edge(UP)
        )

        tracker = ValueTracker(-2*np.pi)

        dot = always_redraw(
            lambda: Dot(
                axes.coords_to_point(
                    tracker.get_value(),
                    amplitude.get_value() * np.sin(tracker.get_value() + phase.get_value())
                ),
                color=RED
            )
        )

        path = TracedPath(dot.get_center, stroke_color=RED)

        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(equation), FadeIn(dot), Create(path))

        self.play(
            tracker.animate.set_value(2*np.pi),
            run_time=4,
            rate_func=linear
        )

        self.play(
            amplitude.animate.set_value(1.8),
            run_time=2
        )
    
        self.play(
            phase.animate.set_value(PI),
            run_time=2
        )

        self.play(
            amplitude.animate.set_value(0.5),
            phase.animate.set_value(2*PI),
            run_time=3
        )
        self.wait()
        #YAY
