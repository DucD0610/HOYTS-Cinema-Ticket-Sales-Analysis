/*CEO: Site traffic breakdown. It has been live for 1 month and we starting to generate sales.
Can you help me to understand where the bulk of our website sessions are coming from? Maybe a breakdown by UTM source, campaign, and referring domain*/
SELECT
	utm_source, utm_campaign, http_referer,
    COUNT(DISTINCT website_session_id) AS number_of_sessions,
	COUNT(DISTINCT website_session_id) / SUM(COUNT(DISTINCT website_session_id))OVER() AS rate
FROM website_sessions
WHERE created_at < '2012-04-14'
GROUP BY utm_source, utm_campaign, http_referer
ORDER BY number_of_sessions DESC;
/*Analysis: After one month of launching, the majority of our traffic came from gsearch for the non-brand campaign taking 97%. 
But did they drive our sales or conversion rate CVR?
*/

SELECT COUNT(DISTINCT w.website_session_id) AS sessions,
		COUNT(DISTINCT o.order_id) AS orders,
        COUNT(DISTINCT o.order_id) / COUNT(DISTINCT w.website_session_id) AS session_to_order_conv_rate
FROM website_sessions w
	LEFT JOIN orders o
		ON w.website_session_id = o.website_session_id
WHERE w.created_at < '2012-04-14'
	AND utm_source = 'gsearch'
    AND utm_campaign = 'nonbrand';
    
/*Analysis: A quick glance shows it's only 2.88% conversion rate which is below 4% threshold the marketing team requires
We are over-spending on the search bids and need to dial down a little bit.
WHAT NEXT? As an analyst: 1)Monitor the impact of bid reductions 2)Analyze performance trending by device type in order to refine bidding strategy */

/*Marketing Manager: We bid down gsearch nonbrand on 2012-04-15. Can you pull gsearch nonbrand session volume by a week to see if the bid changes caused volume to drop at all? */

SELECT 
	YEAR(created_at),
    WEEK(created_at),
    MIN(DATE(created_at)) AS week_started_at, #display the 1st day of the week
	COUNT(DISTINCT website_session_id) AS sessions
FROM website_sessions
WHERE utm_source = 'gsearch'
	AND utm_campaign = 'nonbrand'
    AND created_at < '2012-05-10'
GROUP BY 1,2;
/*Analysis: After the bid down, the data shows there was a decrease in web traffic in the following weeks (16, 18, 19) comparing to the weeks before we made the bid change.
WHAT NEXT? As an analyst: 1)Continue monitoring the volume levels 2)Think how we could make the campaigns more efficient to increase the volume again. */

/*Marketing Manager: Can you pull conversion rate from session to order, by device type? I use our site on my iphone and the user experience was not great.
If desktop performance is better than mobile, we may be able to bid up for desktop to get more volume */
SELECT 
	device_type,
	COUNT(DISTINCT w.website_session_id) AS sessions,
    COUNT(DISTINCT o.order_id) AS orders,
    COUNT(DISTINCT o.order_id) / COUNT(DISTINCT w.website_session_id) AS session_to_order_conv_rate
FROM website_sessions w
	LEFT JOIN orders o
		ON w.website_session_id = o.website_session_id
WHERE w.created_at < '2012-05-11'
	AND utm_source = 'gsearch'
	AND utm_campaign = 'nonbrand'
GROUP BY 1;
/*ANALYSIS: For desktop traffic, it's about 3.73% conversion rate generating revenue for the business. Meanwhile, the CVR of mobile is less than 1%.
We can bid up for desktop to get more value.
Also, it's interesting because the assumption is mobile would be more than desktop due to its convenient nature as users can access our website anywhere, anytime.
However it's lower here. There could be some issues which our mobile app that requires further investigation
 */

/*Tom(Marketing): after the device level analysis of conversion rate, we realized desktop was doing well. So we bid our gsearch nonbrand desktop campaigns up on 2012-05-19.
Can you pull weekly trend for both desktop and mobile so we can check the impact on volume? */
SELECT 
    YEAR(website_sessions.created_at) AS 'year',
    WEEK(website_sessions.created_at) AS 'week',
    MIN(date(website_sessions.created_at)) AS 'date',
    COUNT(DISTINCT CASE WHEN device_type = 'desktop' THEN website_session_id ELSE NULL END) AS desktop_sessions, #pivot method
    COUNT(DISTINCT CASE WHEN device_type = 'mobile' THEN website_session_id ELSE NULL END) as mobile_session
FROM website_sessions
WHERE website_sessions.created_at >= '2012-04-15'
	AND website_sessions.created_at <= '2012-06-10' 
	AND utm_source = 'gsearch'
	AND utm_campaign = 'nonbrand'
GROUP BY 1,2;
#Analysis: At glance, there was indeed an increase in sessions volume after we bid up on 2012-05-19 (week 21, 22, 23,24) comparing to previous weeks (20, 19, 18, 17)

