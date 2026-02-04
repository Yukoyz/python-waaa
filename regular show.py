print('bienvenido al mentor en educacion')
print('obtenga su diploma ahora resolviendo nuestro examen')

print('primera pregunta')

pregunta1=print('¿cual de los siguentes no es cuadrado? ')
opciones=print('a) triangulo', 'b) cuadrado')
respuesta= input(' ').lower().strip()


respuesta_correcta='a'
respuesta_incorrecta='b'

print('\n--- RESULTADO ---')

if respuesta==respuesta_correcta:
    print('respuesta correcta felicidades rigby has obtenido tu diploma')
    print('📜 [DIPLOMA DE EXCELENCIA]')
    
elif respuesta==respuesta_incorrecta:
    print('respuesta incorrecta lo siento rigby no has obtenido tu diploma')

else:
    print('rigby: aaay es muy dificil aaaaa ujudsjusdajaa quiero mi diplomaaaa')

   