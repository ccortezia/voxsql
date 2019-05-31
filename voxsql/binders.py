import textwrap
from .parser import ParsedFrame
from .translators import GenericPythonTranslator


class BaseBinderFactory:

    frame_translator_cls = None

    operation_template = ""

    def create(self, frame: ParsedFrame) -> str:
        translator = self.frame_translator_cls()
        translation = translator.translate(frame)
        opcode = self.operation_template.format(fn=translation)
        return textwrap.dedent(opcode).lstrip()


class Psycopg2BinderFactory(BaseBinderFactory):
    frame_translator_cls = GenericPythonTranslator
    operation_template = """
        def {fn.sign_name}({fn.sign_params}):
            sql_query = {fn.body_sql_query}
            sql_params = {fn.body_sql_params}
            cursor = conn.cursor()
            cursor.execute(sql_query, sql_params)
            fetched = cursor.fetchall()
            cursor.close()
            return {fn.body_return}
        """
