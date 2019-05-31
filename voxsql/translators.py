from dataclasses import dataclass
from .parser import ParsedFrame


@dataclass(frozen=True)
class TranslationData:
    sign_name: str
    sign_params: str
    body_sql_query: str
    body_sql_params: str
    body_return: str


class GenericPythonTranslator:

    def translate(self, frame: ParsedFrame) -> TranslationData:
        return TranslationData(
            self._build_fnsign_name(frame),
            self._build_fnsign_params(frame),
            self._build_fnbody_sql_query(frame),
            self._build_fnbody_sql_params(frame),
            self._build_fnbody_return_statement(frame),
        )

    def _build_fnsign_name(self, frame: ParsedFrame) -> str:
        return frame.header.name

    def _build_fnsign_params(self, frame: ParsedFrame) -> str:
        req_params_strs = []  # TODO: add support for mandatory parameters
        opt_params_strs = [f'{param.name}=None' for param in frame.header.params]
        params_str = ', '.join(['conn'] + req_params_strs + opt_params_strs)
        return params_str

    def _build_fnbody_sql_query(self, frame: ParsedFrame) -> str:
        sql_str = frame.body.source.replace('\n', ' ').strip()
        return f"\"{sql_str}\""

    def _build_fnbody_sql_params(self, frame: ParsedFrame) -> str:
        kwargs_strs = [f'{param.name}={param.name}' for param in frame.header.params]
        kwargs_str = ', '.join(kwargs_strs)
        return f"dict({kwargs_str})"

    def _build_fnbody_return_statement(self, frame: ParsedFrame) -> str:
        if frame.header.retmode == 'scalar':
            return 'fetched[0][0]'
        if frame.header.retmode == 'tuple':
            return 'fetched[0]'
        if frame.header.retmode == 'tuples':
            return 'fetched'
        if frame.header.retmode == 'record':
            fnbody_retvals = [
                f'{retval.name}=fetched[0][{_idx}]'
                for (_idx, retval) in enumerate(frame.header.retvals)
            ]
            fnbody_retvals = ', '.join(fnbody_retvals)
            return f'dict({fnbody_retvals})'
        if frame.header.retmode == 'records':
            fnbody_retvals = [
                f'{retval.name}=row[{_idx}]'
                for (_idx, retval) in enumerate(frame.header.retvals)
            ]
            fnbody_retvals = ', '.join(fnbody_retvals)
            return f'[dict({fnbody_retvals}) for row in fetched]'
        return 'fetched'
