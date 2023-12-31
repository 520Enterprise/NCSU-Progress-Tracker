import * as vscode from 'vscode';

export class CodeTime{
    private userName: string = '';
    private activeTime: number = 0;

    // getToday()
    private userMonth: number = 0;
    private userDay: string = '';
    private userDate: string = '';

    // private feedBack1: string = '';
    private tiredNumber: number = 0;
    // private statusBar: vscode.StatusBarItem = vscode.window.createStatusBarItem(
    //     vscode.StatusBarAlignment.Left,
    // );
    // private showStatusBar: boolean = false;
    private keyNum: number = 0;
    private lineNum: number = 0;


    constructor(){};

    public initialize(): void {
        this.activeTime = new Date().getHours();
        console.log("Initialized: " + this.activeTime);
    }

    public getToday(): string {
        this.userMonth = new Date().getMonth() + 1;
        this.userDay = new Date().getDate().toString();
        if (this.userMonth < 10) {
            this.userDate = 0 + this.userMonth.toString() + this.userDay;
        } else {
            this.userDate = this.userMonth.toString() + this.userDay;
        }
        // console.log('Today is: ' + this.userDate);
        return this.userDate;
    }


    public getUserName() {
        if (vscode.workspace.workspaceFolders) {
            let name = vscode.workspace.workspaceFolders[0].uri.path;
		    this.userName = name.split('/')[2];
        }
        return this.userName;
    }

    public myFunc() {
        // var newMinute = new Date().getMinutes();
        // console.log('Print: ' + newMinute);
        // let userFeedback = vscode.Uri.file('/tmp/CodeTime/' + userDate + '/' + userName + '/feedLog');
		// console.log('Store feedback in: ' + userFeedback);
        let button1 = '1. Not at all';
        let button2 = '2. Slightly';
        let button3 = '3. Medium';
        let button4 = '4. Tired';
        let button5 = '5. Zombie';
        vscode.window.showInformationMessage('How tired are you?', button1, button2, button3, button4, button5)
            .then(selection => {
                if (selection === button1) {
                    console.log('choice 1!');
                    this.tiredNumber = 1;
                    console.log(this.tiredNumber);
                }
                if (selection === button2) {
                    console.log('choice 2!');
                    this.tiredNumber = 2;
                    console.log(this.tiredNumber);
                } 
                if (selection === button3) {
                    console.log('choice 3!');
                    this.tiredNumber = 3;
                    console.log(this.tiredNumber);
                } 
                if (selection === button4) {
                    console.log('choice 4!');
                    this.tiredNumber = 4;
                    console.log(this.tiredNumber);
                }
                if (selection === button5) {
                    console.log('choice 5!');
                    this.tiredNumber = 5;
                    console.log(this.tiredNumber);
                } 
            }
        );
        return this.tiredNumber;
    }

    public getCodeInfo(){
        this.keyNum = 0;
        this.lineNum = 0;
        let editor = vscode.window.activeTextEditor;

        if (editor) {
            vscode.workspace.onDidSaveTextDocument(document => {
                
                this.lineNum = document.lineCount;
                let text = document.getText();
                // TODO: delete command
                let keywords = text.match(/\b(def|if|elif|else|for|while|switch|case|break|continue|return)\b/g);
                if (keywords) {
                    this.keyNum = keywords.length;
                }
                // console.log('Keywords: ' + this.keyNum);
                vscode.window.showInformationMessage(this.keyNum + ' keywords, and ' + this.lineNum + ' lines.');


                const { exec } = require('child_process');
                exec('python3 D:\\Study\\2023Summer\ NCSU\\Coding-Time-Tracker-main\\src\\load_model.py', (err: any, stdout: any, stderr: any) => {
                    if (err) {
                        console.log(err);
                        return;
                    }
                    console.log(stdout);
                    console.log(stderr);
                });


            });
        }
    }



    public dispose(): void {
        this.activeTime = 0;
        console.log("Disposed: " + this.activeTime);
        console.log('extension deactivate');
        console.log('********************');
    }

}
