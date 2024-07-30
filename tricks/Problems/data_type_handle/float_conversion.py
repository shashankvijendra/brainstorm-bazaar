
class FloatValue:
    
    @classmethod
    def decimal_with_zero(value):
        str_value = str(value)
        dot_position = str_value.index('.')
        decimal_part = str_value[dot_position+1:]
        if decimal_part == '0':
            return int(str_value[:dot_position])
        else:
            return float(str_value)

