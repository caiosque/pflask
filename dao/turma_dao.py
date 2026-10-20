from dao.db_config import get_connection

class TurmaDAO:
    sqlSelect = 'SELECT turma.id, semestre, nome_curso, professor.nome FROM turma join curso on curso.id = turma.curso_id join professor on professor.id=turma.professor_id'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        return lista

