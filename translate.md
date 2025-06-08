In my understanding, we want to reduce BP process time to increase Queue resource.

During test, we found there are 4 aspects may should be noticed.

First, in our original thought, we want to short BP process time by decreasing wait_time. But during our test, we found that decrease wait_time can reduce process time of BP, but it's not that directly as our image.
But, during our test, we found that the real waiting time is not equal the setting value. Because the real waiting time is not equal to the setting value. We found this from IBM document, short wait intervals(less than 30 minutes), Sterling B2B places the business process in a special "0" queue. The "0" queue checks every 30 seconds for wait times that have completed and regains an active thread when it reaches its expiration. 

Second, when we short BP process time, it will increase traffic to up/down flow. If we reduce the BP process time but unfortunately there is an unplanned huge traffic into our system. In this case it maybe bring a potential risk to BIS. According to test result, we found that when traffic is increasing, the BIS respond our MDN will be delay. That means there may be a congestion in the BIS.

Additionally, based on queue utilization, reducing the wait time has led to increased pressure on queue resources. As the inbound processing volume has grown, it has also resulted in a corresponding increase in outbound traffic. Under these conditions, more business processes are simultaneously competing for queue resources.

At the same time, the increase in outbound traffic may also place additional resource pressure on the SWIFTNet system.

In addition, we have also explored the use of the sleep method. While it can help reduce the overall wait time more effectively, it tends to consume more queue resources. This is because the sleep method holds the thread for the entire duration until the business process completes.

Therefore, we believe that performance tuning is not as straightforward as simply adjusting the wait_time.

-----------------------------------------------------------------------------------------------------------------------------------
Per my understanding, our main goal is to reduce the BP (Business Process) execution time to help free up queue resources.

During our testing, we noticed that there are four key points we need to be aware of:

First, we thought that just reducing the wait_time would directly shorten the BP processing time. And yes, reducing wait_time can help, but it’s not as straightforward as we imagined.
The actual waiting time didn’t always match what we set. Based on IBM’s documentation, if the wait time is less than 30 minutes, it goes into a special "0" queue, which only checks every 30 seconds. So even if we set a short wait, it might still wait longer than expected.

Second, when BP time gets shorter, the system runs faster — which sounds great — but it also increases both inbound and outbound traffic. If the load spikes suddenly, this can turn into a problem.
In our test, when traffic increased, we saw BIS respond to MDNs more slowly — this might mean the system is getting congested or overloaded.

Third, reducing the wait time puts more stress on queue resources. More BPs finish quickly and then all try to move to the next step at the same time, fighting over limited queue threads. This leads to congestion and slower performance.

Fourth, we also tried using sleep for more precise timing. It is more accurate, but not great performance-wise. That’s because sleep keeps the thread occupied the whole time, which adds more pressure to the queue.

So our conclusion is:
Just changing the wait_time is not enough to improve performance. It’s more complex —  We need to look at the overall system - like queue usage, thread load, and how other systems are impacted like SWIFTNet and BIS. It’s all connected, so we need a balanced strategy without introducing new risks, not just a single change.

-----------------------------------------------------------------------------------------------------------------------------------


Objective and Observations

Our goal is to reduce Business Process (BP) execution time in order to free up and improve utilization of queue resources. During testing, we identified four key aspects that should be carefully considered:

1. Impact of Adjusting wait_time

Initially, we assumed that reducing the wait_time parameter would directly shorten BP execution time. While our tests confirmed that shorter wait_time values can reduce processing duration, the effect is not as immediate or linear as expected.

This is due to the way Sterling B2B Integrator handles short wait intervals (less than 30 minutes). According to IBM documentation, when the wait time is set to under 30 minutes, the system assigns the BP to a special queue ("0" queue). This queue only checks every 30 seconds for completed waits and resumes the process only after the polling interval passes. As a result, the actual wait duration may exceed the configured wait_time.

2. Risk of Increased Upstream and Downstream Traffic

Shortening BP duration can lead to increased system throughput, which in turn raises both inbound and outbound traffic. If this is not carefully managed, especially during unexpected traffic spikes, it can pose a risk to BIS system stability.

During our tests, we observed that when traffic volumes increased significantly, BIS response to MDNs became delayed—indicating possible congestion or processing backlog within BIS.

3. Increased Queue Resource Contention

Reducing wait time also intensifies queue resource usage. As inbound traffic increases, it naturally drives more outbound processing. In this scenario, a greater number of BPs run concurrently, all competing for limited queue threads and resources, further increasing system load and potential delays.

4. Limitations of the sleep Method

We also evaluated the use of the sleep method to control process timing. While this approach can deliver more precise delay behavior compared to Gateway Wait Service, it comes with a trade-off: it holds the processing thread for the entire duration of the wait. This leads to increased thread and queue occupation, reducing overall system efficiency under load.

Conclusion

In conclusion, performance optimization is not as straightforward as adjusting the wait_time parameter alone. Effective tuning requires a comprehensive approach that considers system-wide impacts, including queue utilization, thread occupancy, and downstream effects on systems such as SWIFTNet and BIS. A balanced strategy is essential to ensure both performance gains and system stability.