import math

# --- DATOS DE PRUEBA (Simula una base de datos de alumnos) ---
# Formato: "Nombre, Nota1, Nota2, Nota3, PorcentajeAsistencia"
registro_alumnos = [
    "Carlos Mendoza, 4.5, 3.8, 4.2, 92",
    "Ana Silva, 2.1, 3.0, 1.5, 74",
    "Luis Delgado, 3.5, 3.5, 2.8, 85",
    "María Beltrán, 4.8, 5.0, 4.9, 98",
    "Jorge Rojas, 1.0, 2.0, 1.5, 60"
]

def procesar_reporte(datos):
    """
    Procesa un reporte académico de alumnos con alertas y estadísticas.
    
    Args:
        datos (list): Lista de strings con datos de alumnos
    """
    print("=" * 70)
    print("      REPORTE DE RENDIMIENTO Y ALERTAS ACADÉMICAS")
    print("=" * 70)
    
    todas_las_notas = []
    alumnos_procesados = []
    
    for alumno in datos:
        try:
            # 1. Separar y limpiar los datos de la cadena de texto
            partes = alumno.split(",")
            
            # Validar que hay suficientes datos
            if len(partes) < 5:
                print(f"⚠️ Error: Datos incompletos para '{alumno}'")
                continue
            
            nombre = partes[0].strip()
            n1 = float(partes[1].strip())
            n2 = float(partes[2].strip())
            n3 = float(partes[3].strip())
            asistencia = int(partes[4].strip())
            
            # Validar rangos (notas entre 0 y 5, asistencia 0-100)
            if not (0 <= n1 <= 5 and 0 <= n2 <= 5 and 0 <= n3 <= 5):
                print(f"⚠️ Error: Notas fuera de rango para {nombre}")
                continue
            
            if not (0 <= asistencia <= 100):
                print(f"⚠️ Error: Asistencia inválida para {nombre}")
                continue
            
            # 2. Calcular el promedio ponderado del alumno
            promedio = (n1 + n2 + n3) / 3
            todas_las_notas.append(promedio)
            
            # 3. Lógica del Sistema de Alertas (Condicionales Avanzados)
            estado = "APROBADO"
            alerta = "Ninguna"
            
            if promedio < 3.0 or asistencia < 75:
                estado = "REPROBADO"
                if promedio < 3.0 and asistencia < 75:
                    alerta = "CRÍTICA: Bajo promedio y alta inasistencia"
                elif promedio < 3.0:
                    alerta = "ACADÉMICA: Refuerzo urgente en contenidos"
                else:
                    alerta = "ASISTENCIA: Riesgo de pérdida por faltas"
            
            # Guardar información del alumno
            alumnos_procesados.append({
                'nombre': nombre,
                'promedio': promedio,
                'asistencia': asistencia,
                'estado': estado,
                'alerta': alerta
            })
                    
        except ValueError as e:
            print(f"⚠️ Error al procesar datos numéricos: {e}")
            continue
    
    # Mostrar resultados de alumnos
    for alumno in alumnos_procesados:
        print(f"Estudiante: {alumno['nombre']:<20} | Promedio: {alumno['promedio']:>5.2f} | Asistencia: {alumno['asistencia']:>3}% | {alumno['estado']}")
        if alumno['alerta'] != "Ninguna":
            print(f"   ⚠️ ALERTA -> {alumno['alerta']}")
        print("-" * 70)

    # 4. Estadísticas del Grupo (Uso de funciones matemáticas)
    if todas_las_notas:  # Validar que hay datos
        promedio_grupal = sum(todas_las_notas) / len(todas_las_notas)
        
        # Calcular Desviación Estándar (Mide qué tan dispersas están las notas)
        varianza = sum((x - promedio_grupal) ** 2 for x in todas_las_notas) / len(todas_las_notas)
        desviacion = math.sqrt(varianza)
        
        # Encontrar nota máxima y mínima
        nota_maxima = max(todas_las_notas)
        nota_minima = min(todas_las_notas)
        
        print("\n" + "=" * 70)
        print("                      ESTADÍSTICAS GLOBALES")
        print("=" * 70)
        print(f"Total de Alumnos Procesados: {len(todas_las_notas)}")
        print(f"Promedio General del Grupo:  {promedio_grupal:.2f}")
        print(f"Nota Máxima:                 {nota_maxima:.2f}")
        print(f"Nota Mínima:                 {nota_minima:.2f}")
        print(f"Desviación Estándar:         {desviacion:.2f} (Valores altos indican mucha desigualdad)")
        print("=" * 70)
    else:
        print("⚠️ No hay datos válidos para procesar.")

# Ejecutar el programa
if __name__ == "__main__":
    procesar_reporte(registro_alumnos)
