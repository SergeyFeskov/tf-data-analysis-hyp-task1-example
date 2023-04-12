import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 875744266

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    _, p_val = proportions_ztest([y_success, x_success], [y_cnt, x_cnt], alternative="smaller")
    return p_val < 0.08
