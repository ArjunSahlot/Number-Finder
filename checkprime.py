#
#  Number finder
#  Few codes to tell you what type of number you plugin.
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

num = int(input("Enter a number: "))

if num == 0 or num == 1 or num == 2:
    print("%d is a special number" % num)
    exit(0)

if num & 1 == 0:
    print("%d is not a prime number" % num)
    exit(0)

divisor = 3

while num % divisor != 0:
    divisor=divisor+2
    if divisor >= num/2:
        print("%d is not a prime number" % num)
        break

if divisor <= num/2:
    print("%d is a prime number" % num)