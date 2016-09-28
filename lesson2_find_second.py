def find_second(ss,ts):
    first_index = ss.find(ts);
    second_index = ss.find(ts,first_index+1)
    return second_index
