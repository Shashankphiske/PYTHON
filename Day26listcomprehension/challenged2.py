temperature = {
    "monday":20,
    "tuesday":32,
    "wednesday":25,
    "thursday":38
}

print({key:temperature[key]*9/5 + 32 for key in temperature})