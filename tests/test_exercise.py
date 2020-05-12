import pytest
import src.exercise
import os

def test_exercise():
    os.chdir('src')

    input_values = ["numbers-1.txt","5","20","numbers-1.txt","0","300"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["File?","Lower bound?","Upper bound?","Numbers: 3",\
                      "File?","Lower bound?","Upper bound?","Numbers: 4"]
