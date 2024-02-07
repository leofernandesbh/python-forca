import string
import random
import flet as ft

def letter_to_guess(letter):
    return ft.Container(
        bgcolor=ft.colors.AMBER_500,
        height=50,
        width=50,
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(5),
        content=ft.Text(
            value=letter, 
            color=ft.colors.WHITE,
            size=30,
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD
        ),        
    )

def main(page: ft.Page):
    page.title = "Jogo da Forca"
    page.window_min_width = 490
    page.window_min_height = 1250
    page.bgcolor = ft.colors.BROWN_600
    page.padding = ft.padding.only(left=16, right=16, top=16, bottom=16)
    
    available_words = [
        'python','flet','programador','react','javascript','node',
    ]
    choiced = random.choice(available_words).upper()
    secret_word_len = len(choiced)
    max_attempts = 7
    hits = 0
    
    def validate_letter(e):
        nonlocal hits
        for pos, letter in enumerate(choiced):
            if e.control.content.value == letter:
                hits += 1
                word.controls[pos] = letter_to_guess(letter=letter)
                word.update()
                
        e.control.disabled = True
        e.control.gradient = ft.LinearGradient(colors=[ft.colors.GREY])
        e.control.update()
                
        if e.control.content.value not in choiced:
            victim.data += 1
            victim.src = f'images/hangman_{victim.data}.png'
            victim.update() 
            
        if victim.data == max_attempts:
            page.dialog = ft.AlertDialog(title=ft.Text('\nVocê perdeu! 🥺'), open=True)
            page.update()
        elif hits == secret_word_len:
            page.dialog = ft.AlertDialog(title=ft.Text('\nParabéns! 🥳'), open=True)
            page.update()
    
    victim = ft.Image(
        data=0,
        src='images/hangman_0.png',
        repeat=ft.ImageRepeat.NO_REPEAT,
        height=300
    )
    
    word = ft.Row(
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
           letter_to_guess('_') for _ in choiced
        ]
    )
    
    game = ft.Container(
        col={'xs': 12, 'lg': 6},
        padding=ft.padding.all(50),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                victim,
                word
            ]
        )
    )
    
    keyboard = ft.Container(
        col={'xs': 12, 'lg': 6},
        padding=ft.padding.only(top=130, left=80, right=80, bottom=50),        
        image_src='images/keyboard.png',
        image_repeat=ft.ImageRepeat.NO_REPEAT,
        image_fit=ft.ImageFit.FILL,
        content=ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    height=50,
                    width=50,
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value=letter,
                        color=ft.colors.WHITE,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD
                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.colors.AMBER, ft.colors.DEEP_ORANGE]
                    ),
                    on_click=validate_letter
                ) for letter in string.ascii_uppercase
            ]
        )
    )
    
    scene = ft.Image(col=12, src='images/scene.png')
    
    layout = ft.Column(        
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,        
        controls=[ft.ResponsiveRow(
            columns=12,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                scene                
            ]
        ),
        ft.ResponsiveRow(
            columns=12,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                game,
                keyboard,
            ]
        ),
        ft.ResponsiveRow(
            columns=12,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                scene
            ]
        )]
    )
    
    page.add(layout)        

if __name__ == "__main__":
    ft.app(target=main, assets_dir='assets')
