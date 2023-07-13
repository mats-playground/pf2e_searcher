# pf2e_searcher
A Python program that searches the Pathfinder 2e website's bestiary for images and pulls them all to a local folder. Designed to help dungeon masters make portraits for virtual tabletops without having to manually download the files one-by-one.

## Using the Script
In order to use this script, you need to specify the link under the prefix variable at the very bottom. The two (current) prefixes are:

https://2e.aonprd.com/Monsters (for the Bestiary)
https://2e.aonprd.com/NPCs (for NPCs)

## How It Works
Pathfinder 2e is open source and all of its content is uploaded to the https://2e.aonprd.com website. The monster and NPC directories in particular are sorted in an easily navigable way, by their index.

For example, the link to the Aapoph Serpentfolk is: https://2e.aonprd.com/Monsters.aspx?ID=799

My script runs through the IDs from 0 to 2000, as there are presently less than 2000 entries. As more entries get added, the end index in get_tokens() should be correspondingly updated.

There are sometimes anomalies, especially towards the higher end of 2000. Some indices are skipped. It's possible that there exist anomalous indices beyond 2000, but it's rare, and for the purposes of dungeon master-ing, such anomalies can easily be found manually. Still, it's safe to run at higher indices if you want to cover all your bases. It will just take longer.

## Legal Use
pf2e_searcher uses trademarks and/or copyrights owned by Paizo Inc., used under Paizo's Community Use Policy ([paizo.com/communityuse](paizo.com/communityuse)). We are expressly prohibited from charging you to use or access this content. pf2e_searcher is not published, endorsed, or specifically approved by Paizo. For more information about Paizo Inc. and Paizo products, visit [paizo.com](paizo.com).
