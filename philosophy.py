#!/usr/bin/env python
from random import randint

the_mad_ramblings_of_philosophers = (
    '"The unexamined life is not worth living." - Socrates (470-399 BC)',
    '"Entities should not be multiplied unnecessarily." - William of Ockham (1285-1349)',
    '"The world is my representation." - Arthur Schopenhauer (1788-1860)',
    '"To be able to judge of others by what is present in ourselves--this may be called the art of virtue" - Confucius (551-479 BC)',
    '"The name that can be named is not the eternal name" - Lao Zi (6th century BC)',
    '"Morality is not the doctrine of how we may make ourselves happy, but of how we may make ourselves worthy of happiness" - Immanuel Kant (1724-1804)',
    '"Thought is great and swift and free, the light of the world, and the chief glory of man." - Bertrand Russell (1872-1970)',
    '"The life of man [is] solitary, poor, nasty, brutish, and short." - Thomas Hobbes (1588-1679)',
    '"I think, therefore I am" - Rene Descartes (1596-1650)',
    '"To be is to be perceived" - Bishop George Berkeley (1685-1753)',
    '"We live in the best of all possible worlds." - Gottfried Wilhelm Leibniz (1646-1716)',
    '"The owl of Minerva spreads its wings only with the falling of the dusk." - G.W.F. Hegel (1770-1831)',
    '"Life must be understood backward. But it must be lived forward" - Soren Kierkegaard (1813-1855)',
    '"One cannot step twice in the same river." - Heraclitus (ca. 540-480 BC)',
    '"To understand the things that are at our door is the best preparation for understanding those that lie beyond." - Hypatia (ca. 351-415)',
    '"Don\'t walk behind me, I may not lead. Don\'t walk in front of me, I may not follow. Just walk beside me and be my friend." - Albert Camus (1913-1960)',
    '"You have your way. I have my way. As for the right way, the correct way and the only way--it does not exist." - Friedrich Nietzsche (1844-1900)',
    '"Do not dwell in the past, do not dream of the future, concentrate on the present moment." - Siddhartha Gautama (ca. 563-483 BC)',
    )

print the_mad_ramblings_of_philosophers[randint(0,len(the_mad_ramblings_of_philosophers)-1)]
