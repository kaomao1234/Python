import observerable as ob
import observer as obs
subject = ob.Observable()

observer1 = obs.Observer(subject)
observer2 = obs.Observer(subject)
observer1.bussiness_logic()
subject.notify()
