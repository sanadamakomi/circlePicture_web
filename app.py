# coding:utf-8
# 圆形图制作
from pathlib import Path
from circlePicture import circlePicture
from shiny import App, Inputs, Outputs, Session, reactive, render, ui
from shiny.types import FileInfo, ImgData


app_ui = ui.page_fluid(
    ui.h3(ui.tags.strong("圆形图制作"), style="text-align:center;color:#0000ff;font-size:250%"),
    ui.h6("选择多个图片，截取头像生成圆形图", style="text-align:center"),
    ui.br(),
    ui.row(
        ui.column(8, ui.input_file("file1", "", accept=[".png", ".jpg", ".jpeg"],
                                multiple=True, button_label="浏览", placeholder='未选择文件'),
                  align="center", offset=2),

    ),
    ui.br(),
    ui.row(
        ui.column(8, ui.output_image("image"), align="center", offset=2)
    )
)

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def parsed_file():
        file: list[FileInfo] | None = input.file1()
        if file is None:
            return "请输入图片"
        return [x["datapath"] for x in file if Path(x["datapath"]).exists()]

    @render.image
    def image():
        file_lst = parsed_file()
        dir = Path(__file__).resolve().parent
        circlePicture(dir).run(file_lst)
        out_name = "output.png"
        if Path(str(dir / out_name)).exists():
            img: ImgData = {"src": str(dir / out_name), "width": "800px"}
        else:
            img: ImgData = {"src": str(dir / "default.png"), "width": "200px"}

        return img


app = App(app_ui, server)