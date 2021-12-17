import type { ListItem } from '$lib/utils/types'
import config from '$lib/config'

export const websiteName = config.app.hostname

export const termsOfUse: ListItem[] = [
	{
		title: 'YOUR ACCEPTANCE',
		description:
			`By using or visiting ${websiteName}, you signify your assent to these terms of use. These terms of use ` +
			`apply to all users of ${websiteName}. If you do not agree with these terms of use, then please do not use ` +
			`${websiteName}. If you are unable to understand these terms of use, then please use a translator to do so, ` +
			`or do not use ${websiteName}.`
	},
	{
		title: 'LINKS',
		description:
			`${websiteName} may contain links to third party websites that are not owned or controlled by ${websiteName}. ` +
			`${websiteName} is not affiliated with those websites, has no control over, and assumes no responsibility for, ` +
			`the content, privacy policies, or practices of any third party websites. In addition, ${websiteName} will not ` +
			`and cannot censor or edit the content of any third party site. By using ${websiteName}, you expressly release ` +
			`${websiteName} from any and all liability arising from your use of any third party website. Accordingly, we ` +
			`encourage you to be aware when you have left ${websiteName} and to read the terms and conditions and privacy ` +
			`policy of each other website that you visit. ${websiteName} does not host any of the videos embedded here.`
	},
	{
		title: 'WEBSITE ACCESS',
		description:
			`${websiteName} hereby grants you permission to use ${websiteName}, provided that: (i) your use of ${websiteName} ` +
			`is solely for your personal, noncommercial use; (ii) you will not copy, distribute, or modify any part of ` +
			`${websiteName} without ${websiteName}'s prior written authorization; (iii) you will not send unsolicited or ` +
			`unauthorized advertisements, spam, chain letters, etc; (iv) you will not transmit any content which contains ` +
			`software viruses, or other harmful computer code, files or programs; (v) you will not disrupt servers or networks ` +
			`connected to ${websiteName}; and (vi) you comply with these terms of use. You are solely responsible for the ` +
			`activity that occurs on ${websiteName}. You agree not to use or launch any automated system, including without ` +
			`limitation, 'robots,' 'spiders,' and 'offline readers,' that accesses ${websiteName} in a manner that sends more ` +
			`request messages to its servers in a given period of time than a human can reasonably produce in the same period by ` +
			`using a conventional online web browser. ${websiteName} grants the operators of public search engines permission to use ` +
			`spiders to copy materials from the Website for the sole purpose of creating publicly available searchable indices of the ` +
			`materials, but not caches or archives of such materials. ${websiteName} reserves the right to revoke these exceptions ` +
			`either generally or in specific cases. You agree not to collect or harvest any personally identifiable information, ` +
			`including account names or e-mail addresses, from ${websiteName}. ${websiteName} has the right to terminate your access ` +
			`to the Website, in its sole discretion, immediately and with or without cause.`
	},
	{
		title: 'INTELLECTUAL PROPERTY RIGHTS',
		description:
			`Content on ${websiteName} is provided to you "AS IS" for your information and personal use only and may not be ` +
			`used, copied, distributed, transmitted, broadcast, displayed, sold, licensed, reverse engineered, de-compiled, or ` +
			`otherwise exploited for any other purposes whatsoever without ${websiteName}'s prior written consent. ${websiteName} ` +
			`reserves all rights not expressly granted in and to ${websiteName}. If you download or print a copy of the content for ` +
			`personal use, you must retain all copyright and other proprietary notices contained therein.`
	},
	{
		title: 'COPYRIGHT AND CONTENT POLICY',
		description:
			`${websiteName} respects the intellectual property rights of others and requests you to do the same. ${websiteName} does ` +
			`not permit infringement of intellectual property rights on its platform, and will promptly suspend commercial content ` +
			`(served via a publicly available web address / URL) from being able to be converted and downloaded by its platform when ` +
			`kindly notified. If you are a content creator/owner, copyright owner, or an agent thereof and would like to disable the ` +
			`possible use of ${websiteName}'s platform to convert your publicly available content(s), please kindly send us a request ` +
			`via creating an issue on Github at ${config.app.github} with the following information: the URL(s) and description(s) ` +
			`of the content(s) you want us to block; a form of electronic or physical evidence showing that you have the rights to act for ` +
			`the content(s); contact information taht is reasonably sufficient to permit us to contact you, such as an address, telephone ` +
			`number, and a valid e-mail address. The relevent content(s) will be blacklisted in our system within 24 hours.`
	},
	{
		title: 'WARRANTY DISCLAIMER',
		description:
			`You agree that your use of the website shall be at your sole risk to the fullest extent permitted by law, ${websiteName} ` +
			`, its owner, and agents disclaim all warranties, express or implied, in the connection with ${websiteName} and your use ` +
			`thereof. ${websiteName} makes no warranties or representations about the accuracy or completeness of the websites content ` +
			`and assumes no liability for any (i) mistakes or inaccuracies of content, (ii) personal injury or property damage resulting ` +
			`from your use of ${websiteName}, (iii) any unauthorized access to our use of our servers and/or any and all peronsal information ` +
			`stored therein, (iv) any interruption or cessation of transmission to or from ${websiteName}, (v) any bugs, viruses, trojan ` +
			`horses, or the like which may be transmitted to or through ${websiteName} by any third party, and/or (vi) any errors or ` +
			`omissions in any content or for any loss or damage of any kind incurred as a result of the use of any content on or via ` +
			`${websiteName}. ${websiteName} does not warrant, endorse, or assume any responsibility for any content, or product, or service ` +
			`advertised or offered by a third party through ${websiteName} or featured in any advertising, and ${websiteName} will not be ` +
			`a party to or in any way be responsible for monitoring any transaction between you and third party providers of products or ` +
			`services. You agree that your use of ${websiteName} shall be at the unique purpose of converting and downloading content ` +
			`for restrictive and personal uses. As the service is fully accessible from the internet, you agree that you need to know the ` +
			`specific rules applied in your country. You agree taht more generally all the content downloaded from ${websiteName} is intended ` +
			`for an evaluation period and will not be present on your device or any other devices more than a restrictive period of 2 days. ` +
			`You agree that if you wish to keep the content and if this content is sold under a license, then you will purchase a license of it.`
	},
	{
		title: 'LIMITATION OF LIABILITY',
		description:
			`In no event shall ${websiteName}, its owners, or agents, be liable to you for any direct, indirect, incidental, special, ` +
			`punitive, or consequential damages whatsoever resulting from any (i) content, including any mistakes or inaccuracies therein, ` +
			`(ii) personal injury or property damage, of any nature whatsoever resulting from your use of ${websiteName}, (iii) any unauthorize ` +
			`use of our server and/or any and all personal information stored therein, (iv) any interruption or cessation of transmission ` +
			`to or from ${websiteName}, (v) any bugs, viruses, trojan horses, or the like which may be transmitted to or through ${websiteName} by ` +
			`any third party, and/or (vi) any errors or omissions in any content or for any loss or damage of any kind incurred as a result of the ` +
			`use of any content on or via ${websiteName}, whether based on warranty, contract, tort, or any other legal theory, and whether or ` +
			`not ${websiteName} is advised of the possiblity of such damages. The foregoing limitation of liability shall apply to the fullest ` +
			`extent permitted by law in the applicable jurisdiction. You specifically acknowledge that ${websiteName} shall not be liable for user ` +
			`submissions or the defamatory, offensive, or illegal conduct of any third part and that the risk of harm or damage from the foregoing ` +
			`rests entirely with you.`
	},
	{
		title: 'INDEMNITY',
		description:
			`You agree to defend, indemnify and hold harmless ${websiteName}, its owner, and agents, from and against any and all claims, damages, ` +
			`obligations, losses, liabilities, costs and expenses (including but not limited to attorney's fees) arising from: (i) your use of ` +
			`${websiteName}; (ii) your violation of these terms of use; (iii) your violation of any third party right, including without limitation ` +
			`any copyright, property, publicity or privacy right; or (iv) any claim that one of your submissions caused damage to a third party. ` +
			`This defense and indemnification obligation will survive these terms of use and your use of the ${websiteName}.`
	},
	{
		title: 'ABILITY TO ACCEPT TERMS OF USE',
		description:
			`You affirm that you are either more than 18 years of age or possess legal parental or guardian consent to enter into these terms of use, ` +
			`and to comply with these terms of use. In any case, you affirm that you are over the age of 13, as ${websiteName} is not intended for ` +
			`children under 13. If you are under 13 years of age, then please do not use ${websiteName}.`
	},
	{
		title: 'ASSIGNMENT',
		description:
			`These terms of use, and any rights and licenses granted hereunder, may not be transferred or assigned by you, but may be assigned by ` +
			`${websiteName} without restriction.`
	}
]
