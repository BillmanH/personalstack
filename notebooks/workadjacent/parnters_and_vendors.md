# Partner Ecosystems
_When you lose control of your data, you lose control of the pace and timing of innovation._
## How to assess the fitness of a 3rd party vendor for your enterprise data solution.

I'm often brought into meetings to explore bringing a new 3rd party vendor into an enterprise data system. As an Azure Architect and Data Analyst with more than 10 years in the industry, I have a lot of hands-on experience building and integrating platforms into a production-ready data platform. Partners, the right ones, offer a lot to an enterprise in terms of accelerating digital transformation and enabling analysts. The wrong ones create silos while tying up your enterprise IT budget. 

If you are an IT Decision Maker (ITDM), this should help you think about the vendor you are considering and how they are positioned. Most importantly how they can help you and at what cost. If you are a vendor, this should be helpful in designing a product that meets your enterprise customer needs and not create a burden on their long-term plans.


## Your IT landscape

In an oversimplification, your enterprise problems look like this:

![default arch](../../docs/img/blog/default.png?raw=true)

You have these three large capability areas. Your end goal is so that end users have access to the information that they need and are satisfied with how they get it. 

However, while you do manage groups of IT engineers who manage your data platform, you aren't a software development company and don't plan to make this your focus. You want your teams to have the best tools in the industry, and the best quality data, without having to build everything from scratch yourself. 

![default arch](../../docs/img/blog/notasoftwareco.png?raw=true)

You shouldn't try to build everything yourself. That would be a waste of resources. Even if you had the technical capability to do so. Many companies have been working on these problems and are way ahead of you. You want to focus on the problems that are unique to your company and buy solutions from vendors who solve industry-wide problems. 

Here come vendors with those solutions. 

![default arch](../../docs/img/blog/entervendors.png?raw=true)

Vendors solve every kind of data infrastructure problem in existence (or at least offer to). 

## Vendor Archetypes

### The End-to-End Solution
Some vendors see themselves as the beginning and the end of data transformation. They are unaware of other systems or believe that there shouldn't be any other platforms than the one they are offering.

![default arch](../../docs/img/blog/thebigpartner.png?raw=true)

The risk: You won't have access to any of your data unless it is in a way that was designed by the vendor. 

The ideal customer: The company that doesn't see data as part of its strategic IP and wants to outsource it as much as possible. Also assumes that the client is OK with following the industry when new features are added, rather than getting in front.

It is a matter of strategic direction to decide at what level you will innovate, and what levels of control you are willing to let go of. Your team will still have quality tools and the vendor will have the responsibility of keeping up to date. There will be progress, but you won't control the pace and timing of that progress. It could be the case that an end-to-end vendor, who has control of your data, won't feel as pressured to innovate knowing that you can't easily leave. However, in a growing vendor there could be incentive in that future customers would see the progress that you are making. Deciding what you won't do is as important as deciding what you will do. 

In a way, Azure and AWS are examples of the end-to-end partner. However, they offer connections at every step. You can buy the whole solution, or just parts. There are many ways to access the data in every stage of the contextualization. While they offer analytics and reporting tools, they don't prevent you from innovating your own OR inviting other 3rd party vendors where there exists a better solution. 

What to verify in the pitch meeting:
* Where does the data live?
* Other than your amazing dashboard, what other APIs and tools exist to access data? 
* Can you query the data itself, or just the pipelines that are provided to you? 
* If you want to introduce another vendor to part of the solution. 


### The Big Ego
Sometimes the vendor has a competitive advantage in an area but isn't really focused on enterprise deployments. This is common in data science and analytics tools where the people at that end focus on visualization and insights but don't know much about enterprise engineering. 

![default arch](../../docs/img/blog/the_big_ego.png?raw=true)

The risk: You will spend much more time integrating this platform than you would a more conventional system.

The ideal customer: The team that manages this tool doesn't have a lot of other systems to manage. The team that owns version control in this tool doesn't also manage your versioning tools in other areas, for example. 

What to verify in the pitch meeting:
* How does it manage version control?
* At some point they will show you a process to create "custom business logic". That part of the presentation will be brief and vague. Inquire further. The reason they aren't speaking to that process is because there are only ten people in the world who know how to do that part.
* Can it use common, open-source frameworks? Even if it uses a framework that your team doesn't know, there will be resources like Stack Overflow, GitHub, and many other where the community has been active for years. 

Pay attention vendors: It might be easier to leverage the common, open frameworks that people have been using for years. The version-control system isn't part of your core competency anyways. Better to just differ to the open conventions. If you create your own process, you must support it, and that will take your energy away from what you do well. 


# The ideal partner
The ideal partner, in any relationship, adds value without forcing you to become dependent. With enterprise data partnerships this means enriching your data or simplifying a process, without taking control or ownership of your enterprise data. 

![default arch](../../docs/img/blog/best_partner.png?raw=true)

When done poorly, you can end up with a vendor that controls your data while tying you into an agreement that you can't get out of. This is common. This creates an additional silo where you can't access data outside of the tools provided to you. Remember that **you want data so that you can find unique ways to solve business problems**. I've personally seen many IT data strategies fail because they have been tied up in a system that controls their data for them. In most cases the only way to develop new capabilities is to open a support ticket or pay them to upgrade their product. 

When you lose control of your data, you lose control of the pace and timing of innovation. Innovation becomes the thing that the vendor does, not you. And they will innovate at their own schedule if they feel that it would be costly to migrate. They control the direction and strategy, not you.

Great examples of true partners: DataBricks, DBT Labs, Azure-ML. All of these add value-add tools to your data stack but take no control. Your data stays with you. You can use any cloud, or any combination of tools and it won't interrupt those services. They aren't greedy. Regardless of what you think about these platforms, they all have:
* Use the SDK to operate from version control CICD pipelines.
* Use the Web-UI to do your work, they will generate code that you can submit to conventional version control. 
* Designed to be part of an ecosystem, not the entire ecosystem. 


## Conclusion

At the enterprise level, third party tools are an important part of a data platform. ITDMs should review the features and understand what they bring to the table and what they take away. Think about the vendor you are listening to and try to understand how they fit into your infrastructure, and how they can help or hurt your ecosystem. 
