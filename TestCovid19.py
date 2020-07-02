print('=' * 80)
print('Programa para diagnostico de pacientes con sintomas compatibles con COVID-19. ')
print('=' * 80)


edad = int(input('Ingrese la edad del paciente: '))
temperaturaCorporal = int(input('ingrese la temperatura del paciente: '))
print('Presione la tecla "s" si el paciente tiene neumonia evidenciada o "n" en caso contrario')
neumonia = input()


if neumonia == 's':
    print()
    print('Es un caso sospechoso. El paciente debera quedar internado...')
elif neumonia == 'n':
    
    if temperaturaCorporal > 37:
        print('Responda las siguientes preguntas presionando la tecla "s" para SI o "n" para NO')
        tos = input('Tiene el paciente tos?: ')
        if tos == "s":
            tos = True
        elif tos == 'n':
            tos = False
        else:
            print('Ha presionado un valor incorrecto..')
        
        odinofagia = input('tiene el paciente odinofagia?: ')
        if odinofagia == 's':
            odinofagia = True
        elif odinofagia == 'n':
            odinofagia = False
        else:
            print('Ha presionado un valor incorrecto..')
        
        dificultadRespiratoria = input('Dificultad respiratoria ?: ')
        if dificultadRespiratoria == 's':
            dificultadRespiratoria = True
        elif dificultadRespiratoria == 'n':
            dificultadRespiratoria = False
        else:
            print('Ha presionado un valor incorrecto..')

        if tos or odinofagia or dificultadRespiratoria:
            
            personalSalud = input('Es el paciente personal de salud?: ')
            if personalSalud == 's':
                personalSalud = True
            elif personalSalud == 'n':
                personalSalud = False
            else:
                print('Ha presionado un valor incorrecto..')
            
            contactoCovid = input('Estuvo el paciente en contacto con casos positivos de COVID-19?: ')
            if contactoCovid == 's':
                contactoCovid = True
            elif contactoCovid == 'n':
                contactoCovid = False
            else:
                print('Ha presionado un valor incorrecto..')
            
            viajoExterior = input('Ha viajado al exterior en los ultimos 14 dias?: ')
            if viajoExterior == 's':
                viajoExterior = True
            elif viajoExterior == 'n':
                viajoExterior = False
            else:
                print('Ha presionado un valor incorrecto..')
            
            transmisionesLocales = input('Ha estado el paciente en zonas locales de transmision confimadas?: ')
            if transmisionesLocales == 's':
                transmisionesLocales = True
            elif transmisionesLocales == 'n':
                transmisionesLocales = False
            else:
                print('Ha presionado un valor incorrecto..')
            

            if personalSalud:
                print()
                print('Es un caso sospechoso por ser personal de salud con dos o mas sintomas asociados al COVID-19.')
            elif contactoCovid:
                print()
                print('Es un caso sospechoso por presentar dos o mas sintomas y haber tenido contacto con casos confimados.')
            elif viajoExterior:
                print()
                print('Es un caso sospechoso por presentar dos o mas sintomas y haber viajado al exterior en los ultimos 14 dias')
            elif transmisionesLocales:
                print()
                print('Es un caso sospechoso autoctono por presentar dos o mas sintomas y haber estado en zonas de transmision local.')
            else:
                print()
                print('Es un caso sospechoso por presentar dos o mas sintomas asociados al COVID-19.')

        else:
            print()
            print('El paciente no presenta suficientes sintomas para considerarlo de riesgo. sin embargo tiene fiebre por lo que debera ser monitoreado a diario.')


    else:
        if edad >= 60:
            print()
            print('El paciente no es un caso sospechoso pero debe cuidarse dado que es grupo de riesgo.')
        else:
            print()
            print('El paciente no es un caso sospechoso porque no presenta ninguno de los sintomas asociados.')
        
else:
    print('Ha presionado un valor incorrecto..')