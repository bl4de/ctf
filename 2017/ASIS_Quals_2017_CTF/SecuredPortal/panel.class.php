<?php
/**
 * panel Class
 *
 * @category  controller
 * @author    ?????
 */

class panel extends main {

    /**
     * holds authentication status of the user
     * @var boolean
     */
    private $__auth;

    /**
     * holding database object
     * @var object
     */
    private $__db;

    /**
     * checking authentication string
     *
     * @param string object
     */
    function __construct($db){
        $this->__db = $db;
        $sessionString = null;

        /**
         * gathering authentication string by auth parameter in HTTP request
         */
        if(array_key_exists('auth', $_GET))
            $sessionString = $_GET['auth'];

        if(strlen($sessionString) > 32){
            $signature = substr($sessionString, -32);
            $payload = base64_decode(substr($sessionString, 0, -32));

            /**
             * real signature calculation based on the key
             */
            $realSign = md5($payload.$this->__sessionKey);

            /**
             * making it impossible to login, if the site is under maintenance,
             */
            if(__MAINTENANCE__===true)
                $realSign = substr($realSign, 0, 6);

            /**
             * checking signature, prevent to data forgery by user
             */
            if($realSign == $signature){
                $this->data = unserialize($payload);

                if(is_array($this->data)){
                    /**
                     * checking login status
                     */
                    if($this->data['logged']===true){
                        $this->__auth = true;
                    }
                }
            }
        }
    }

    /**
     * index
     */
    function index(){
        if(!$this->__auth){
            echo 'login required';
            return false;
        }

        template('panel');
    }

    /**
     * send http request to contact server, after the validity of message format is checked, we will look at messages in paper print
     */
    function flag(){
        if(!$this->__auth){
            echo 'login required';
            return false;
        }

        /*
         * WOW, SEEMS THE FLAG IS HERE :)
         */
        require 'includes/flag.php';
    }

    /**
     * downloading source code via last changes
     */
    function downloadSource(){
        if(!$this->__auth){
            echo 'login required';
            return false;
        }

        $file = '../source.zip';
        if (file_exists($file)){
            header('Content-Description: File Transfer');
            header('Content-Type: application/x-gzip');
            header('Content-Disposition: attachment; filename="'.basename($file).'"');
            header('Expires: 0');
            header('Cache-Control: must-revalidate');
            header('Pragma: public');
            header('Content-Length: ' . filesize($file));
            readfile($file);
            exit;
        }
    }

    /**
     * send http request to contact server, after the validity of message format is checked, we will look at messages in paper print
     */
    function contact(){
        if(!$this->__auth){
            echo 'login required';
            return false;
        }

        /**
         * setting fullName to anonymous or the real name
         */
        $this->fullName = 'anonymous';
        if(@$this->data['title'] == 'mr.' or @$this->data['title'] == 'ms.')
            $this->fullName = $this->data['title'] . $this->data['username'];

        /**
         * setting fullName to anonymous or the real name
         */
        if(array_key_exists('contactUs', $_POST)){
            if(array_key_exists('message', $_POST))
                $message = $_POST['message'];

            /*
             * check message validity
             */
            $userCurl = (new userCurl(__SERVER_2, $message))->sendPOST();

            /*
             * printing response to the user
             */
            if($userCurl==='valid')
                echo json_encode(array('name'=>json_encode($this->fullName), 'status'=>true, 'message'=>'We have received you message, our administrator will be reading your issue as soon as possible'));
            else
                echo json_encode(array('name'=>json_encode($this->fullName), 'status'=>false, 'message'=>'It seems the message sent is not in the valid format.', 'error'=>$userCurl));
        }
    }
}