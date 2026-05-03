

from class4 import Camera_Trap

#ii. Create two instances
leopard = Camera_Trap("Leopard", "Forest", 3)
elephant = Camera_Trap("Elephant", "Riverside",3)

#iii. Record several captures
leopard.record_capture()
leopard.record_capture()
leopard.record_capture()

elephant.record_capture()
elephant.record_capture()

#iv. Test check_target and print
print(leopard.check_target()) #complete
print(elephant.check_target()) # incomplete

#v. Add both to a list
traps = [leopard, elephant]

#v.display table
print(f"\n{"Species":<10}{"Location:":<12}{"Captures":<10}{"Target":<8}{"Status"}")
print("-"* 60)

for trap in traps:
    print(f"{trap.name:<10}{trap.location:<12}{trap.capture_count:<10}{trap.target_count:<8}{trap.check_target()}")
