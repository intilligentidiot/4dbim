<?php
/**
 * Simple PHP Contact Form Handler
 * 
 * HOW TO USE SMTP (for better deliverability):
 * 
 * 1. Why SMTP?
 *    The standard PHP mail() function used below often sends emails that land in Spam folders
 *    because they lack proper authentication (SPF/DKIM). SMTP uses a real email server 
 *    (like Gmail, Outlook, or your host) to send mail securely.
 * 
 * 2. Prerequisite: PHPMailer
 *    To use SMTP, you typically need a library called PHPMailer.
 *    Run this command in your terminal if you have Composer installed:
 *    > composer require phpmailer/phpmailer
 * 
 * 3. Configuration
 *    Once installed, you would replace the mail() function below with:
 *    
 *    $mail = new PHPMailer\PHPMailer\PHPMailer();
 *    $mail->isSMTP();
 *    $mail->Host = 'smtp.gmail.com';  // Specify main and backup SMTP servers
 *    $mail->SMTPAuth = true;          // Enable SMTP authentication
 *    $mail->Username = 'your-email@gmail.com'; 
 *    $mail->Password = 'your-app-password'; 
 *    $mail->SMTPSecure = 'tls';       // Enable TLS encryption, `ssl` also accepted
 *    $mail->Port = 587;               // TCP port to connect to
 * 
 */

// Configuration
$to_email = "admin@bim4dservices.com"; // REPLACE WITH YOUR EMAIL
$subject_prefix = "[Website Inquiry] ";

// Only process POST requests
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // 1. Sanitize and Validate Inputs
    $name = strip_tags(trim($_POST["name"]));
    $name = str_replace(array("\r", "\n"), array(" ", " "), $name);

    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);

    $message = trim($_POST["message"]);

    // Check for empty fields or invalid email
    if (empty($name) OR empty($message) OR !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400); // Bad Request
        echo "Please complete the form and try again.";
        exit;
    }

    // 2. Prepare Email Content
    $subject = $subject_prefix . "New message from $name";

    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n\n";
    $email_content .= "Message:\n$message\n";

    // 3. Prepare Email Headers
    $headers = "From: $name <$email>";

    // 4. Send Email
    if (mail($to_email, $subject, $email_content, $headers)) {
        http_response_code(200);
        // You can redirect to a Thank You page here if you prefer:
        // header("Location: thank-you.html");
        echo "Thank You! Your message has been sent.";
    } else {
        http_response_code(500); // Internal Server Error
        echo "Oops! Something went wrong and we couldn't send your message.";
    }

} else {
    // Not a POST request, display a 403 forbidden
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
?>