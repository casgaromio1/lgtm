import click

@click.command()
def cli():
    """LGTM 이미지 생성도구"""
    lgtm()
    click.echo('lgtm') # 동작 확인용
    
def lgtm():
    # 여기에 로직을 추가해 나감
    pass