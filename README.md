# diffusion-be-indexer-task

At Diffusion, we are seeking a proficient backend engineer to join our growing team. The role requires a strong understanding of software architecture, experience programming in object-oriented languages such as Golang or Rust, as well as an intermediate understanding of Python. The role will focus on building fast and robust systems for data processing, and will interface directly with cloud engineering and frontend development teams.

This task mirrors the core responsibilities of a backend engineer at Diffusion and is focussed on building a prototype data system. It deals with indexing swaps on the Ethereum network, ensuring consistent formatting, and local storage of swaps in an appropriate database structure. Successful applicants will use tools like Pydantic in Python for data integrity, handling multiple pool addresses concurrently, and highlighting scalability concerns.

Here are some key points to consider:

#### Task Description

Build a system to index historic swaps on Ethereum, and create a queryable database for historic swaps.

Things to consider should include: How to include the dollar value of swaps and their execution price, how to include the cost of each transaction in gas terms and also in dollar terms.

#### Desirables and Considerations

- Utilize tools like Pydantic for ensuring data consistency and type safety.
- Implement asynchronous querying of the blockchain node for improved efficiency.
- Design a mechanism to order swaps chronologically to construct a complete timeseries of swap data.
- Consider scalability by extending functionality to handle multiple pool addresses simultaneously.
- Provide an indicative suitable unit testing framework to test the functionality of this submission.

#### Bonuses

- Develop a robust error handling mechanism for edge cases or network disruptions during data retrieval.
- Optimize the indexing process for faster data extraction without compromising accuracy.
- Implement data validation mechanisms to ensure the integrity of retrieved swap information.
- Explore potential optimizations for storage, such as database integration or compression techniques.

This summary outlines the task to index historical swaps from the Ethereum network, standardize their structure, and store them locally, emphasizing data consistency, efficiency, and scalability. Candidates are encouraged to consider additional improvements and optimizations beyond the outlined scope for bonus points.

### Submission

Candidates are encouraged to submit their completed tasks in a programming language they prefer, with Python, Rust, or Golang being the preferred choices. Submissions can be sent to `jake` at `diffusion` dot `io`. 

Alternatively, candidates can grant email access or provision their submission in a private repository accessible to this email to review the task. This flexibility allows candidates to showcase their proficiency in their preferred language while ensuring ease of submission and evaluation for the backend engineer role at Diffusion.

### Example

The file `example.py` provides a quick script to query swaps executed on a **specific pool** within the last 2000 blocks on the Ethereum network. The specific pool queried is the pool at the contract address `0x0d4a11d5EEaaC28EC3F61d100daF4d40471f1852` on the network.

The following data gives detail on the position of the transaction which contained the swap in the block. This is important to ensure that swaps are ordered correctly:

```
Transaction Hash:       0xcf0571d98d9dc548fe8276e6f8c88dbaff9f218388172607ec1a33ecb3c2f13c
Transaction Index:      49
Block Number:           18924041
```

Alongside this block data, the response also contains the parameters of the indexed event itself:
```
{'sender': '0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD', 'to': '0x0cFB06414C6d9790Bc661230DbA0b24060808bF4', 'amount0In': 81276700000000000, 'amount1In': 0, 'amount0Out': 0, 'amount1Out': 192429009}
```

These parameters detail the amounts of tokens (in decimals) which were transferred as part of the swap event.
