## Los alumnos y el asesor

Se decidió resolver el problema de los alumnos y el asesor. Se utilizó el lenguaje Python 3 y el editor de texto VS Code. Para ejecutar el programa, únicamente hay que ejecutar el siguiente comando, tomando en cuenta que Python 3 se encuentra instalado:

    $ python los_alumnos_y_el_asesor.py


La estrategia utilizada para resolver el problema fue muy similar a la utilizada en el problema de productor-consumidor. Es decir, se utilizó un mutex para proteger el buffer y un semáforo para tomar en cuenta el número de elementos en éste y esperar por nuevos si es que está vacío.

Uno de los requerimientos del programa era que el profesor "durmiera" si no había ningún alumno, lo cual se cumple fácilmente gracias a que, si el semáforo tiene un valor de cero, el profesor únicamente se bloqueará hasta que se agregue un estudiante al buffer. De igual forma, es relevante mencionar que se utilizó una cola para el buffer, debido a la naturaleza del problema: una vez que el alumno realiza una pregunta, es enviado al último lugar de la fila para que así sus compañeros puedan realizar preguntas lo más pronto posible.

Por último, el productor se implementó agregando periódicamente estudiantes al salón de clases. Si éste está lleno, se mostrará un mensaje indicando que el estudiante fue rechazado; de lo contrario, se añadirá al salón de clases.

Nos surgió una duda respecto a la implementación: al momento de que el profesor está procesando las preguntas de los alumnos, notamos que si no colocábamos un sleep después de liberar el mutex no se añadían los nuevos estudiantes. Inferimos que lo anterior se debe a que en la siguiente iteración se vuelve a adquirir el mutex inmediatamente, sin dar oportunidad a que el otro hilo añada los estudiantes. ¿Cómo se podría solucionar esto o cuál sería la forma correcta de hacerlo?