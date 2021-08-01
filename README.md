# discord-nitro-generator

This program will generate discord nitro gift links. It will do so by generating a 16 character code.

It creates 2 files:
The first file is ``alreadyGenerated.txt`` , which will contain links you have already generated. That way you do not generate the same link twice. You can also paste a list of links (Or just the 16 digit codes) that you know are invalid into this file. That way the program does not generate those links either.

The second file is ``links.txt``, this will contain the output of the program. The links will be in the format ``https://discord.gift/code``. So the links you generate. Each time you start the program again, this file will be whiped and only contain the newly generated links. The old links will still be present in ``alreadyGenerated.txt`` to prevent them from generating again.
