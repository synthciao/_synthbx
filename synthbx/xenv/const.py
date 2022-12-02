class ESuffix():
    VDT_INSERT = '_vdt_insert'
    VDT_DELETE = '_vdt_delete'
    SDT_INSERT = '_sdt_insert'
    SDT_DELETE = '_sdt_delete'
    EVL_UPDATE = '_evl_update'
    UPDATE = '_update'
    ALIAS = '__cp'


class EPrefix():
    FLAG_V = 'Fv__'
    FLAG_R = 'Fr__'
    AUX = 'Au'
    VAR = 'v'
    ANOVAR = 'a__'
    MIDDLE_REL = 'M__'


class ESymbol():
    FLAG_V = '"_valid_"'
    FLAG_R = '"_rejected_"'
    NULL = '"_null_"'


class EExt():
    FACT = '.facts'
    EXPT = '.expected'
    CSV = '.csv'
    SC = '.sc'


class EFolder():
    EXAMPLE = 'example'
    GCANDIDATE = 'gcandidate'
    SCHEMA = 'schema'
    RESULT = 'result'
    SYNTH = 'synth'
    GET = '_get'
    PUT = '_put'


class EFile():
    GET = 'get.dl'
    PUT = 'put.dl'
    DGET = 'dget.dl'
    CGET = 'cget.dl'
    CPUT = 'cput.dl'


class ESynth():
    CANDIDATE_RULE_DL = 'rules.small.dl'
    RULENAME_TXT = 'ruleNames.small.txt'
    SOUFFLE_EXE = 'synthbx/souffle/souffle'
    PROSYNTH_PY = 'synthbx/core/prosynth.py'
