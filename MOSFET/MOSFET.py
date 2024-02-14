from manim import *
CM_PER_INCH = 2.54


def config_frame(width, height, dpi: int = 300, frame_rate: int = 30, video_dir: str = None):
    from math import ceil
    if not video_dir:
        video_dir = '{media_dir}/videos/{module_name}/' + f'{dpi}dpi{frame_rate}'
    config.frame_rate = frame_rate
    config.video_dir = video_dir
    dpc = dpi / CM_PER_INCH
    config.frame_width, config.frame_height = width, height
    config.pixel_width, config.pixel_height = map(ceil, [config.frame_width * dpc, config.frame_height * dpc])
    # The pixel width and height must be divisible by 2.
    if config.pixel_width & 1:
        config.pixel_width += 1
    if config.pixel_height & 1:
        config.pixel_height += 1


class CreateMOS(Scene):
    def construct(self):
        points_base = [LEFT * 1 + UP * 0.75, LEFT * 1, RIGHT * 1, RIGHT * 1 + UP * 0.75]
        points_n = [LEFT * 1 + UP * 0.75, LEFT * 1 + UP * 0.5, RIGHT * 1 + UP * 0.5, RIGHT * 1 + UP * 0.75]
        points_ed = [LEFT * 1 + UP * 1, LEFT * 1 + UP * 0.75, LEFT * 0.5 + UP * 0.75, LEFT * 0.5 + UP * 1]
        points_es = [RIGHT * 1 + UP * 1, RIGHT * 1 + UP * 0.75, RIGHT * 0.5 + UP * 0.75, RIGHT * 0.5 + UP * 1]
        points_eg = [LEFT * 0.25 + UP * 1.05, LEFT * 0.25 + UP * 0.8, RIGHT * 0.25 + UP * 0.8, RIGHT * 0.25 + UP * 1.05]
        points_oxi = [LEFT * 0.25 + UP * 0.8, LEFT * 0.25 + UP * 0.75, RIGHT * 0.25 + UP * 0.75, RIGHT * 0.25 + UP * 0.8]

        square_base = Polygon(*points_base, color=GREEN, fill_opacity=1, stroke_width=0)
        square_n = Polygon(*points_n, color=YELLOW, fill_opacity=1, stroke_width=0)
        square_ed = Polygon(*points_ed, color=GRAY, fill_opacity=1, stroke_width=0)
        square_es = Polygon(*points_es, color=GRAY, fill_opacity=1, stroke_width=0)
        square_eg = Polygon(*points_eg, color=GRAY, fill_opacity=1, stroke_width=0)
        square_oxi = Polygon(*points_oxi, color=BLACK, fill_opacity=1, stroke_width=0)

        mosfet = VGroup(square_base, square_n, square_es, square_eg, square_ed, square_oxi)

        # 绘制 MOS
        self.play(FadeIn(mosfet))
        self.wait()


class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class AnimateMOS(Scene):
    def construct(self):
        points_base = [LEFT * 1 + UP * 0.75, LEFT * 1, RIGHT * 1, RIGHT * 1 + UP * 0.75]
        points_n = [LEFT * 1 + UP * 0.75, LEFT * 1 + UP * 0.5, RIGHT * 1 + UP * 0.5, RIGHT * 1 + UP * 0.75]
        points_ed = [LEFT * 1 + UP * 1, LEFT * 1 + UP * 0.75, LEFT * 0.5 + UP * 0.75, LEFT * 0.5 + UP * 1]
        points_es = [RIGHT * 1 + UP * 1, RIGHT * 1 + UP * 0.75, RIGHT * 0.5 + UP * 0.75, RIGHT * 0.5 + UP * 1]
        points_eg = [LEFT * 0.25 + UP * 1.05, LEFT * 0.25 + UP * 0.8, RIGHT * 0.25 + UP * 0.8, RIGHT * 0.25 + UP * 1.05]
        points_oxi = [LEFT * 0.25 + UP * 0.8, LEFT * 0.25 + UP * 0.75, RIGHT * 0.25 + UP * 0.75, RIGHT * 0.25 + UP * 0.8]

        square_base = Polygon(*points_base, color=GREEN, fill_opacity=1, stroke_width=0)
        square_n = Polygon(*points_n, color=YELLOW, fill_opacity=1, stroke_width=0)
        square_ed = Polygon(*points_ed, color=GRAY, fill_opacity=1, stroke_width=0)
        square_es = Polygon(*points_es, color=GRAY, fill_opacity=1, stroke_width=0)
        square_eg = Polygon(*points_eg, color=GRAY, fill_opacity=1, stroke_width=0)
        square_oxi = Polygon(*points_oxi, color=BLACK, fill_opacity=1, stroke_width=0)

        mosfet = VGroup(square_base, square_n, square_es, square_eg, square_ed, square_oxi)

        # MOS 动画
        points = [LEFT * 1 + UP * 0.5, LEFT * 1, RIGHT * 1, RIGHT * 1 + UP * 0.5]
        lines = VGroup(*[Line(points[i], points[i + 1]) for i in range(3)])
        arc = ArcBetweenPoints(points[-1], points[0], angle=56*DEGREES)
        lines.set_stroke(width=0)
        arc.set_stroke(width=0)
        quadrilateral = VGroup(lines, arc)
        quadrilateral.set_fill(GREEN, opacity=1)

        # 创建直线
        arc1 = ArcBetweenPoints(points[-1], points[0], angle=TAU / 12)
        arc1.set_stroke(width=0)
        qua_target = VGroup(lines, arc1)
        qua_target.set_fill(GREEN, opacity=1)

        # 定义电极之间的连接线
        vg_line = Line(UP * 1.05, UP * 1.25).append_points(Line(UP * 1.25, UP * 1.25 + RIGHT * 1.75).points)
        vs_line = Line(UP * 0.875 + LEFT * 1, UP * 0.875 + LEFT * 1.25).append_points(
            Line(UP * 0.875 + LEFT * 1.25, DOWN * 0.25 + LEFT * 1.25).points
        ).append_points(
            Line(DOWN * 0.25 + LEFT * 1.25, DOWN * 0.25 + RIGHT * 1.75).points
        )
        vb_line = Line(ORIGIN, DOWN * 0.4)
        vd_line = Line(UP * 0.875 + RIGHT * 1, UP * 0.875 + RIGHT * 1.1)

        # 定义信号标签
        gnd_label = Text("Gnd", font_size=12).next_to(vb_line, DOWN, buff=0.1)
        vgs_brace = BraceBetweenPoints(vg_line.get_end(), vs_line.get_end(), RIGHT, buff=SMALL_BUFF)
        vgs_label = Tex("$V_{gs}$", font_size=24).next_to(vgs_brace, RIGHT, buff=0.1)
        vds_brace = BraceBetweenPoints(vd_line.get_end(), DOWN * 0.25 + RIGHT * 1.1, RIGHT, buff=SMALL_BUFF)
        vds_label = Tex("$V_d$", font_size=24).next_to(vds_brace, RIGHT, buff=0.1)

        # 数值指示
        vgs_eq = Text("=", font_size=12).next_to(vgs_label, RIGHT, buff=0.1)
        number = DecimalNumber().set_color(BLUE).scale(0.5).next_to(vgs_eq, RIGHT, buff=0.1)
        # number.add_updater(lambda num: num.move_to(vgs_label, RIGHT))

        # 显示四边形
        self.add(mosfet)
        self.add(quadrilateral)
        points_mask_l = [LEFT * 1 + UP * 0.75, LEFT * 1 + UP * 0.5, LEFT * 0.5 + UP * 0.5, LEFT * 0.5 + UP * 0.75]
        points_mask_r = [RIGHT * 0.5 + UP * 0.75, RIGHT * 0.5 + UP * 0.5, RIGHT * 1 + UP * 0.5, RIGHT * 1 + UP * 0.75]
        self.add(Polygon(*points_mask_l, color=YELLOW, fill_opacity=1, stroke_width=0))
        self.add(Polygon(*points_mask_r, color=YELLOW, fill_opacity=1, stroke_width=0))
        self.add(vg_line, vs_line, vb_line, vd_line, Dot(DOWN * 0.25),vgs_brace, vds_brace, gnd_label)
        self.add(vgs_label, vds_label)
        self.add(vgs_eq, number)
        self.play(Count(number, 0, 5), Transform(quadrilateral, qua_target), run_time=5, rate_func=linear)
        # self.play(Transform(quadrilateral, qua_target), run_time=4, rate_func=linear)
        self.wait()
        self.add(mosfet)
        self.add(qua_target)
        points_mask_l = [LEFT * 1 + UP * 0.75, LEFT * 1 + UP * 0.5, LEFT * 0.5 + UP * 0.5, LEFT * 0.5 + UP * 0.75]
        points_mask_r = [RIGHT * 0.5 + UP * 0.75, RIGHT * 0.5 + UP * 0.5, RIGHT * 1 + UP * 0.5, RIGHT * 1 + UP * 0.75]
        self.add(Polygon(*points_mask_l, color=YELLOW, fill_opacity=1, stroke_width=0))
        self.add(Polygon(*points_mask_r, color=YELLOW, fill_opacity=1, stroke_width=0))
        self.add(vg_line, vs_line, vb_line, vd_line, Dot(DOWN * 0.25),vgs_brace, vds_brace, gnd_label)
        self.add(vgs_label, vds_label)
        points = [LEFT * 1 + UP * 0.5, LEFT * 1, RIGHT * 1, RIGHT * 1 + UP * 0.5]
        lines = VGroup(*[Line(points[i], points[i + 1]) for i in range(3)])
        arc = ArcBetweenPoints(points[-1], points[0], angle=56*DEGREES)
        lines.set_stroke(width=0)
        arc.set_stroke(width=0)
        quadrilateral = VGroup(lines, arc)
        quadrilateral.set_fill(GREEN, opacity=1)
        self.play(Count(number, 5, 0), Transform(qua_target, quadrilateral), run_time=4, rate_func=linear)
        self.wait()


if __name__ == '__main__':
    config.preview = True  # 渲染完成后自动打开文件
    config.format = "gif"
    config_frame(width=7.11, height=4, dpi=300, frame_rate=30)
    scene = AnimateMOS()
    scene.render()
