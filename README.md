 Lifeline Aid 

A beacon for refugees in conflict zones. Instantly see nearby food, shelter, and aid. Get alerts on regional hazards. Direct links to humanitarian agencies. Hope in chaos.

## Purpose / Movitation

This project was created for [Cal Hacks 10.0](https://www.calhacks.io/), an hackathon ran by University of California, Berkeley. The app serves as a beacon for refugees in conflict zones, where affected users can use this app to locate official places that offer humanitarian aid and other essentials (eg. food and water). 

This project is developed by Javier Miranda, Noelle Wang, Andres Yllescas and Ashly Benitez within the 30 hour time limit of Cal Hacks.

## The "techy side"

This repo serves as a monorepo, most notably these two folders:

- `multiNew` - The React Native (TS) mobile app as the frontend
- `fastapi-backend` - FastAPI application (Python w/ type hints) that uses [CockroachDB](https://www.cockroachlabs.com/). `asyncpg`-based project, as CockroachDB natively implements the PGWire Protocol (in simply terms, CockroachDB fully supports any and all PostgreSQL drivers and code).

As a part of a sponsership deal, UC Berkeley partnered up with CockroachLabs in order to provide a prize for whoever which team uses CockroachDB the best. Up to $2000 dollars.

### Mobile app

The choice of framework for us would be React Native. We needed something to deploy both to APple devices and Android devices, as people in these countries do not have easy access to the web. The mobile app presented the challenge of learning said framework, but the intergration between the mobile app and backend. 

Development of the mobile app were led by Javier Miranda and Andres Yllescas.

### Backend

Originally seltting on Django, we figured out that using Django meant wasting more time and the restrictions imposed on ORMs. After noticing the 5.8x (or 580%) performance boost over psycopg2 and 5x (or 500%) over psycopg3 (and 8.2x or 820% faster than node-js), it made sense to break out the big guns - asyncpg. Used by over 40,000 developers, asyncpg's users contain projects such as [R. Danny](https://github.com/Rapptz/RoboDanny), which are known to be extremely stable and performant. For reasons described above, along with fimliarly with asyncpg, the decision was set to switch over. 

The backend implements a connection pool of 25, which is suitable for most instances. All connections are pulled from the pool and sent back once finished. 

## The future of the app

Ultimately, this app is not finished. There are plans to maintain this as an UCMACM project, continuing the legacy of Lifeline Aid. Plans include:

- User auth
- Rewrite of some of the core parts
- User forums

and many many more.




