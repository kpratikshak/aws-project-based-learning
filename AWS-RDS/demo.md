## AWS DynamoDB Global Tables - Multi-Region, Multi-Active Replication

👋 # Global Tables:
Global Tables for Amazon DynamoDB provides replication with multi-region tables that are replicated to and active in all regions that you select. Every region's replica is Active, Hence, there are no read replicas in Global Tables.

Your applications are communicating with the local replica, but all your data is replicated by DynamoDB to all of the regions you have selected for that global table.

You can convert your existing single-region table to a global table with no downtime. 
You can easily add a remove table as a global table and all your data is encrypted at rest.

The table must use on-demand capacity mode or if you are using provisioned capacity mode then auto-scaling must be enabled.

DynamoDB Global table replicas are inter-connected, but not interdependent - Tables replicas are connected and do exchange data, but their functioning and maintenance are not dependent on each other. In case, If something happens to a global table in region-A it does not affect the other global table replicas in other regions.

Writes in one replica are replicated in all other replicas.
Usually, the data is propagated to other regions within one second.

Eventually consistent across all tables.

Uses the Last Writer Wins reconciliation to reconcile the conflicts (Last Writer Wins reconciliation ? Whichever replica that writes the latest version wins and will be propagated to all other replicas)

What do DynamoDB Global Tables offer
High Availability.

More Durability.

Better Fault Tolerance.

In Disaster Recovery (DR) Planning Terms (RTO/RPO): your database would meet a recovery time objective of near zero and a recovery point objective of about one second.

Uptime SLA of 99.999%

Setup & Operation
You can use any of the below to operate everything related to DynamoDB global table.

AWS Console.
CDK.
API/SDK.
CLI.
Cloud Formation.
How to Create a Global Table in AWS Console & See the Data Getting Replicated.
Create a DynamoDB Table. In my case, I have created a table named BookCatalog with 3 attributes.

BookName
Author
Genre


Make sure to enable either on-demand capacity mode or provision capacity mode with auto-scaling. Also, since the Global tables use DynamoDB Streams to facilitate replication, make sure to enable DynamoDB streams.

Once you are done with the above setup, Navigate to the Global Tables tab and click on the Create Replica button to create a replicate of your DynamoDB Table.


Select the region you want the replica to be created and Click Create. This will now create a replica of your DynamoDB table in the specified region along with any data in there are data also in the table. Otherwise, the table only will get replicated.


Now, navigate to DynamoDB table in the us-wast-2 region to see your replicated data.

![creation-dynamodb-table](https://github.com/user-attachments/assets/f7260f1b-1ac6-4b8e-8604-7600fe435c1c)
![templates](https://github.com/user-attachments/assets/c0b1f166-1737-488d-b77a-9456875f9af8)
![connection-options](https://github.com/user-attachments/assets/0badeaee-0a0f-4dbc-b588-98b3c65990f0)

![gateway_endpoint](https://github.com/user-attachments/assets/293cd773-52e7-49ba-96a0-ef565df615ea)
![dynamodb-endpoint](https://github.com/user-attachments/assets/08dd0a79-3717-4ca5-9089-93076a535190)
![aws-rds-snapshot](https://github.com/user-attachments/assets/664f123e-e1ca-44cb-823c-f2875eb7229a)
