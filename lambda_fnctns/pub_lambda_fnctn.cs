using System.Text;
using System.Web;


namespace pub_lambda_fnctn
{
	const string accountSID = "accountSID";
	const string authToken = "authtoken";

	TwilioClient.Init(accountSID, authToken); 

	try { 
		var message = MessageResource.Create(
			// Need a way to retrieve user phone numbers from dictionary objects
			// the "to" number must be verified
			to: new PhoneNumber(userPhoneNum));
		// Really hoping this isn't someone's actual phone number. 
		from: new PhoneNumber("+9998887777");
		body: // scraper.getInfo() or something, need a way to retrieve from objects in database
	}
	catch (TwilioException ex) { 
		Console.WriteLine(Exception.Message); 
	}
}