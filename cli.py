import click
import os
import functions

@click.command()
@click.option("--mode", "-m", type=str, default="", help="Modos disponibles: secuencial | multihilo | multiprocesos", is_flag=False, flag_value="")
@click.option("--photos", "-p", type=int, help="Número de fotos", is_flag=False, flag_value="")
@click.pass_context
def mode(ctx, mode, photos):
    # Error shown if the user enters something that is not on the list
    if mode not in ["secuencial", "multihilo", "multiprocesos", None, ""]:
        ctx.fail("Debe seleccionar un modo de ejecución válido")
    else:
        if mode == "secuencial":
            print("Ejecutando modo secuencial")
            functions.secuencial(photos)
        elif mode == "multihilo":
            print("Ejecutando modo multihilo")
            # functions.multihilo(photos)
        elif mode == "multiprocesos":
            print("Ejecutando modo multiprocesos")
            # functions.multiprocesos(photos)
        elif mode == None or mode == "": # If there's no mode selected, execute all modes
            print(f"Ejecutando todos los modos, numero de fotos es {photos}")
            functions.secuencial(photos)
            functions.multihilo(photos)
            functions.multiprocesos(photos)





if __name__ == "__main__":
    mode()