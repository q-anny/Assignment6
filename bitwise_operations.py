import sys

try:
  integers = [int(value) for value in sys.argv[1].split(',')]
  threshold = int(sys.argv[2]) 
except ValueError:
  print("<span>All numbers and threshold must be integers</span>")
  sys.exit()

bitwise_and = integers[0]
bitwise_or = integers[0]
bitwise_xor = integers[0]

for current_integer in integers[1:]:
  bitwise_and &= current_integer
  bitwise_or |= current_integer
  bitwise_xor ^= current_integer

filtered = [integer for integer in integers if integer > threshold]

html_output = (
  f"<p>Bitwise AND: {bitwise_and}</p>"
  f"<p>Bitwise OR: {bitwise_or}</p>"
  f"<p>Bitwise XOR: {bitwise_xor}</p>"
  f"<p>Values gratear than threshold: {filtered}</p>"
)

print(html_output)