def calculate_grade(score):
    if score < 0 or score > 100:
        return "Error: La puntuación debe estar entre 0 y 100."
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# El usuario introduce la puntuación antes de llamar a la función
score_input = float(input("Introduce la puntuación del examen (0-100): "))
grade = calculate_grade(score_input)
print(f"La calificación correspondiente es: {grade}")