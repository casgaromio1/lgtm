import click

@click.command()
@click.option("--message", "-m", default="LGTM",
              show_default=True, help="이미지에 추가할 문자열")
@click.argument("keyword")
def cli(keyword, message):
    """LGTM 이미지 생성도구"""
    lgtm()
    click.echo('lgtm') # 동작 확인용
    
def lgtm(keyword, message):
    # 여기에 로직을 추가해 나감
    pass