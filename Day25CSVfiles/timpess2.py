from sympy import symbols, residue, sin

# Define the variable and function
z = symbols('z')
f = z/z*(z-3)

# Compute the residue
res = residue(f, z, 3)  # Residue at z = 1j

# Print the result
print("Residue at z = 1j:", res)



