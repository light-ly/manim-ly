from manim import *


class CreateMOS(Scene):
    def construct(self):
        # 基底矩形
        points_base = [LEFT * 1 + UP * 0.75, LEFT * 1, RIGHT * 1, RIGHT * 1 + UP * 0.75]
        square_base = Polygon(*points_base, color=GREEN, fill_opacity=1, stroke_width=0)

        # N 区矩形
        points_n = [LEFT * 1 + UP * 0.75, LEFT * 1 + UP * 0.5, RIGHT * 1 + UP * 0.5, RIGHT * 1 + UP * 0.75]
        square_n = Polygon(*points_n, color=YELLOW, fill_opacity=1, stroke_width=0)

        # 电极矩形
        points_ed = [LEFT * 1 + UP * 1, LEFT * 1 + UP * 0.75, LEFT * 0.5 + UP * 0.75, LEFT * 0.5 + UP * 1]
        points_es = [RIGHT * 1 + UP * 1, RIGHT * 1 + UP * 0.75, RIGHT * 0.5 + UP * 0.75, RIGHT * 0.5 + UP * 1]
        points_eg = [LEFT * 0.25 + UP * 1.05, LEFT * 0.25 + UP * 0.8, RIGHT * 0.25 + UP * 0.8, RIGHT * 0.25 + UP * 1.05]
        points_oxi = [LEFT * 0.25 + UP * 0.8, LEFT * 0.25 + UP * 0.75, RIGHT * 0.25 + UP * 0.75, RIGHT * 0.25 + UP * 0.8]

        square_ed = Polygon(*points_ed, color=GRAY, fill_opacity=1, stroke_width=0)
        square_es = Polygon(*points_es, color=GRAY, fill_opacity=1, stroke_width=0)
        square_eg = Polygon(*points_eg, color=GRAY, fill_opacity=1, stroke_width=0)
        square_oxi = Polygon(*points_oxi, color=BLACK, fill_opacity=1, stroke_width=0)

        mosfet = VGroup(*square_base, *square_n, *square_es, *square_eg, *square_ed, *square_oxi)

        # 绘制 MOS
        self.play(FadeIn(mosfet))
        self.wait()


class AnimateMOS(Scene):
    def construct(self):
        # 基底矩形
        points_base = [LEFT * 1 + UP * 0.75, LEFT * 1, RIGHT * 1, RIGHT * 1 + UP * 0.75]
        square_base = Polygon(*points_base, color=GREEN, fill_opacity=1, stroke_width=0)

        # N 区矩形
        points_n = [LEFT * 1 + UP * 0.75, LEFT * 1 + UP * 0.5, RIGHT * 1 + UP * 0.5, RIGHT * 1 + UP * 0.75]
        square_n = Polygon(*points_n, color=YELLOW, fill_opacity=1, stroke_width=0)

        # 电极矩形
        points_ed = [LEFT * 1 + UP * 1, LEFT * 1 + UP * 0.75, LEFT * 0.5 + UP * 0.75, LEFT * 0.5 + UP * 1]
        points_es = [RIGHT * 1 + UP * 1, RIGHT * 1 + UP * 0.75, RIGHT * 0.5 + UP * 0.75, RIGHT * 0.5 + UP * 1]
        points_eg = [LEFT * 0.25 + UP * 1.05, LEFT * 0.25 + UP * 0.8, RIGHT * 0.25 + UP * 0.8, RIGHT * 0.25 + UP * 1.05]
        points_oxi = [LEFT * 0.25 + UP * 0.8, LEFT * 0.25 + UP * 0.75, RIGHT * 0.25 + UP * 0.75, RIGHT * 0.25 + UP * 0.8]

        square_ed = Polygon(*points_ed, color=GRAY, fill_opacity=1, stroke_width=0)
        square_es = Polygon(*points_es, color=GRAY, fill_opacity=1, stroke_width=0)
        square_eg = Polygon(*points_eg, color=GRAY, fill_opacity=1, stroke_width=0)
        square_oxi = Polygon(*points_oxi, color=BLACK, fill_opacity=1, stroke_width=0)

        mosfet = VGroup(*square_base, *square_n, *square_es, *square_eg, *square_ed, *square_oxi)

        points = [LEFT * 1 + UP * 0.5, LEFT * 1, RIGHT * 1, RIGHT * 1 + UP * 0.5]
        lines = VGroup(*[Line(points[i], points[i + 1]) for i in range(3)])
        arc = ArcBetweenPoints(points[-1], points[0], angle=TAU / 6)
        lines.stroke_width = 0
        arc.stroke_width = 0
        quadrilateral = VGroup(*lines, arc)
        quadrilateral.set_fill(GREEN, opacity=1)

        # 创建直线
        arc1 = ArcBetweenPoints(points[-1], points[0], angle=TAU / 12)
        lines.stroke_width = 0
        arc1.stroke_width = 0
        qua_target = VGroup(*lines, arc1)
        qua_target.set_fill(GREEN, opacity=1)

        # 显示四边形
        self.add(mosfet)
        self.add(quadrilateral)
        self.play(Transform(quadrilateral, qua_target), run_time=10)
        self.wait()
