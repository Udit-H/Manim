from manim import *
import numpy as np

class IntegralScene(Scene):
    def construct(self):
        integral = MathTex(
            r"\int_{e^2}^{e^4}",
            r"\frac{e^{(\ln^2 x + 1)^{-1}}}{e^{(\ln^2 x + 1)^{-1}} + e^{((6 - \ln x)^2 + 1)^{-1}}}",
            r"\frac{dx}{x}"
        )

        integral.scale(1.2)
        integral.move_to(ORIGIN)

        self.play(Write(integral))
        self.wait(3)

        integral_small = integral.copy().scale(0.6).to_corner(UL)
        self.play(Transform(integral,integral_small))
        self.wait(2)

        axes = Axes(x_range=[0,100,10], y_range = [0,1.5], x_length = 6, y_length = 5, axis_config={"include_tip":True})
        axes.shift(RIGHT*3.5,UP*1.2)
        axes_labels = axes.get_axis_labels(x_label = "X", y_label = "Y")
        func = lambda x: np.exp(-1 / (np.log(x)**2 + 1)) / (
            np.exp(-1 / (np.log(x)**2 + 1)) + np.exp(-1 / ((6 - np.log(x))**2 + 1)))
        e2_label = MathTex(r"e^2").next_to(axes.c2p(np.exp(2), 0), DOWN)
        e4_label = MathTex(r"e^4").next_to(axes.c2p(np.exp(4), 0), DOWN)
        graph = axes.plot(func,color = BLUE)
        area = axes.get_area(graph, x_range = [np.exp(2),np.exp(4)],color = ORANGE,opacity = 0.5)
        self.play(DrawBorderThenFill(axes),Write(axes_labels))
        self.play(Create(graph))
        self.play(Write(e2_label),Write(e4_label))
        self.wait(1.5)
        self.play(FadeIn(area))
        self.wait(2)

        subs = MathTex(r"Let \ln x = t \\",
                       r"\implies \frac{1}{x} \, dx = dt \\",
                       r"x = e^2, \, t = \ln e^2 = 2 \\",
                       r"x = e^4, \, t = \ln e^4 = 4"
        )
        subs.scale(0.6)
        subs.move_to(integral)
        self.play(subs.animate.next_to(integral,DOWN).to_edge(LEFT))
        self.wait(2)

        step1 = MathTex(
            r"I = \int_{2}^{4}",
            r"\frac{e^{(t^2  + 1)^{-1}}}{e^{(t^2  + 1)^{-1}} + e^{((6 - t)^2 + 1)^{-1}}}",
            r"dt").scale(0.8).next_to(subs,DOWN).to_edge(LEFT)
        self.play(Write(step1))
        self.wait(2)

        step2 = MathTex(
            r"I = \int_{2}^{4}",
            r"\frac{e^{((6 - t)^2 + 1)^{-1}} + e^{(t^2  + 1)^{-1}}}{e^{(t^2  + 1)^{-1}}}",
            r"dt").scale(0.8).next_to(step1,DOWN).to_edge(LEFT)
        self.play(Write(step2))
        self.wait(2)

        combined = MathTex(
            r"I + I = \int_{2}^{4}",
            r"\frac{e^{(t^2 + 1)^{-1}} + e^{((6 - t)^2 + 1)^{-1}}}{e^{(t^2 + 1)^{-1}} + e^{((6 - t)^2 + 1)^{-1}}}",
            r"dt"
        ).scale(0.8).next_to(subs, DOWN).to_edge(LEFT)
        self.play(Transform(step1, combined), Transform(step2, combined))
        self.wait(2)

        simplified = MathTex(
            r"2I = \int_{2}^{4} 1 \, dt"
        ).scale(0.8).next_to(combined, DOWN).to_edge(LEFT)
        self.play(Write(simplified))
        self.wait(2)

        finalstep = MathTex(r"I = \frac{2}{2} = 1"
        ).scale(0.8).next_to(simplified,DOWN).to_edge(LEFT)
        self.play(Write(finalstep))
        self.wait(2)
