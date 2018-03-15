# rokers-hunting-razerblade

This the repository with the solution to the [Reply Code Challenge](https://challenges.reply.com/tamtamy/challenge/5/detail) provided by the rokers team.

### The Project Logo

"There is no GitHub project without a logo"  -- [Gianpaolo Macario](https://gmacario.github.io/), 2018

![logo](logo.png)

**Acknowledgements**: The logo has been gently created by [Scott Lewis](https://thenounproject.com/iconify/) from Noun Project.

### The Project Charter

* [x] (M.0) Build up the Project Team
* [x] (M.0) Read and understand the [Reply Code Challenge rules](https://challenges.reply.com/tamtamy/page/platformRules.action)
* [x] (M.0) Read and understand the [Terms and Conditions for RC18](https://challenges.reply.com/tamtamy/documents/challenges/RC18_World_Terms&Condition.pdf)
* [x] (M.1) Agree on the Project Rules
* [ ] (M.2) [Have Fun]( https://github.com/ludusrusso/rokers-hunting-razerblade/issues/12)
* [ ] (M.2+) ...
* [ ] (M.NaN) Profit!

### The Project Team

(Please keep entries sorted by GitHub_ID)

| GitHub_ID                                            | Firstname        | Lastname      | Telegram_ID      | Notes |
|------------------------------------------------------|------------------|---------------|------------------|-------|
| [@FiorellaSibona](https://github.com/FiorellaSibona) | Fiorella         | Sibona        | @fiorella_sibona | -     |
| [@gmacario](https://github.com/gmacario)             | Gianpaolo        | Macario       | @gmacario        | -     |
| [@ludusrusso](https://github.com/ludusrusso)         | Ludovico Orlando | Russo         | @ludusrusso      | -     |
| [@xrmx](https://github.com/xrmx)                     | Riccardo         | Magliocchetti | ?                | -     |

### The Project Rules

1. We (the Project Team) only code in Python
2. No Project Team member can leave the Project before completion of [M.2](https://github.com/ludusrusso/rokers-hunting-razerblade/milestone/3)
3. All the communications between the Project Team members take place using one of the following channels:
   - Issues and Pull Requests on GitHub project [ludusrusso/rokers-hunting-razerblade](https://github.com/ludusrusso/rokers-hunting-razerblade)
   - Messages on the Telegram group "ROKERS hunting for a Razer Blade"
   - Chat inside the [JOL](https://github.com/ludusrusso/rokers-hunting-razerblade/issues/10)
4. Any change to the Project Rules follows the Change Management process described below
5. The Only (remaining) Rule Is That [There Are No Rules](https://www.youtube.com/watch?v=YN0WTpEZn3w)

### Change Management Process

* Any Team Member may propose a change to the Project Rules above by creating a [new Issue](https://github.com/ludusrusso/rokers-hunting-razerblade/issues/new).
* The change must be reviewed and approved by all the other Project Team members.
* If the change is approved, the proposer shall update this document by means of a corresponding [Pull Request](https://github.com/ludusrusso/rokers-hunting-razerblade/pulls).

### How to use the program

#### Execute the program as a Jenkins pipeline

1. Install [easy-jenkins](https://github.com/gmacario/easy-jenkins)
2. Install Jenkins pipeline

#### Execute the program on a Raspberry Pi

```
pi@rpi3gm23:~/github/rokers-reply/rokers-hunting-razerblade$ docker run -v $PWD:/app -w /app python:3.6.4-alpine3.6 python3 parsing.py
pi@rpi3gm23:~/github/rokers-reply/rokers-hunting-razerblade$
```

### License and Copyright

See [`LICENSE`](LICENSE).

<!-- EOF -->
