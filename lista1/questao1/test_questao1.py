from lista1 import questao_1, questao_2
import numpy as np

def read_matrix_from_file(file_path):
    with open(file_path, 'r') as f:
        inputs = f.read().split(';\n')
        converted_inputs = []
        for i in inputs:
            if len(i) > 1:
                converted_inputs.append(list(map(float, i.split(','))))
        return converted_inputs
        
def test_question_1(func = questao_1, tests_location = 'comp1-2022-tests/lista1/questao1'):
    inputs = read_matrix_from_file('input')
    targets = read_matrix_from_file('output')
    outputs = []
    
    for i in inputs:
        outputs.append(func(*i))
    
    try:
        np.testing.assert_allclose(np.copy(targets).flatten(), np.copy(outputs).flatten(), verbose=False)
    except AssertionError as e:
        mask = (np.copy(targets) == np.copy(outputs))
        e.add_note((f'\n WRONG ELEMENTS POSITIONS: {np.argwhere(mask == False)[:,0]}'))
        e.add_note((f'\n CORRECT ELEMENTS POSITIONS: {np.argwhere(mask != False)[:,0]}'))
        # raise(Exception((f' CORRECT ELEMENTS POSITIONS: {np.argwhere(mask != False)[:,0]}')))
        raise(e)
        
test_question_1()

