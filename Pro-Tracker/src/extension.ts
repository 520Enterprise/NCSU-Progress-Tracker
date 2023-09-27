import * as vscode from "vscode";
import { ProgressLocation } from "vscode";
import { TextDecoder, TextEncoder } from "util";
import * as path from "path";

import { CodeTime } from "./codetime";
const { performance } = require("perf_hooks");
const { execFile } = require('child_process');

async function fileExist(fileUri: vscode.Uri) {
    try {
        await vscode.workspace.fs.stat(fileUri);
        return true;
    } catch {
        return false;
    }
}

async function readFile(fileUri: vscode.Uri) {
    let exist = await fileExist(fileUri);
    if (exist) {
        let buffer = await vscode.workspace.fs.readFile(fileUri);
        return new TextDecoder().decode(buffer);
    } else {
        return "Coding events:";
    }
}

async function getFeedback() {
    let feedback1: string | undefined = await vscode.window.showInputBox({
        prompt: "How tired do you feel now? (please choose from 1-5)",
    });
    if (feedback1) {
        console.log(feedback1);
        return feedback1;
    }
}

function calculateMedian(predictions: number[]): number {
    predictions.sort((a, b) => a - b);
    const middle = Math.floor(predictions.length / 2);
    if (predictions.length % 2 === 0) {
        return (predictions[middle - 1] + predictions[middle]) / 2;
    } else {
        return predictions[middle];
    }
}

var assignments = {
    "homework1.py": "hw1",
    "homework2.py": "hw2",
    cylinder_volume: "hw3",
    test_cylinder_volume: "hw3",
    shipping_rate: "hw4",
    test_shipping_rate: "hw4",
    hailstone: "hw5",
    alphabetical: "hw7",
    sum_list: "hw8",
    input_tracker: "hw9",
    count_character: "hw10",
    test_count_character: "hw10",
    pair_max: "hw11",
    plot_stats_for_test: "hw12",
    "inlab1.py": "lab1",
    "inlab2.py": "lab2",
    cube_volume: "lab3",
    substract_discount: "lab3",
    testing_cube_volume: "lab3",
    testing_substract_discount: "lab3",
    largest_of_two: "lab4",
    largest_of_three: "lab4",
    A_test_largest_of_two: "lab4",
    A_test_largest_of_three: "lab4",
    B_test_largest_of_two: "lab4",
    B_test_largest_of_three: "lab4",
    C_test_largest_of_two: "lab4",
    C_test_largest_of_three: "lab4",
    cumulative_sum: "lab5",
    average_entries: "lab5",
    testing_cumulative_sum_1: "lab5",
    testing_cumulative_sum_2: "lab5",

    // ... 添加其他的映射关系 ...
};

var codetime: CodeTime;

function generateProgressBar(completionPercentage: number): string {
    const totalBars = 10;
    const completedBars = Math.round((completionPercentage / 100) * totalBars);

    // Create the progress bar string
    const progressBar = '*'.repeat(completedBars) + '_'.repeat(totalBars - completedBars);

    return progressBar;
}

function updateStatusBarWithFunctionNames(
    document: vscode.TextDocument,
    position: vscode.Position
) {
    const functionPattern = /^def ([a-zA-Z_][a-zA-Z0-9_]*)\(/gm; // Python函数定义的正则表达式
    const content = document.getText(); // 文档的内容

    let match;
    let lastFunctionName = "None"; // 默认值
    while ((match = functionPattern.exec(content))) {
        const functionName = match[1];
        const functionStartPos = document.positionAt(match.index);
        if (functionStartPos.isBefore(position)) {
            // 如果函数定义的开始位置在光标之前，则更新函数名
            lastFunctionName = functionName;
        } else {
            // 如果函数定义的开始位置在光标之后，直接跳出循环
            break;
        }
    }
    var homeworkName = "None";
    if ((assignments as any)[lastFunctionName]) {
        homeworkName = (assignments as any)[lastFunctionName];
    }

    let fileName = path.basename(document.fileName);
    console.log("Current file: " + fileName);
    if ((assignments as any)[fileName]) {
        homeworkName = (assignments as any)[fileName];
    }

    

    console.log('loading model...');

    const model_loaderPath = path.join(__dirname, 'model_loader.py');


    // path is like model/hw1/hw1_completion_lasso_model.joblib
    const models = ['lasso', 'ridge', 'random_forest', 'svr'];
    var predictions: number[] = [];
    var medianCompletion: number = 0;

    for (const modelName of models) {
        const modelFilePath = path.join(__dirname, 'model', homeworkName, `${homeworkName}_completion_${modelName}_model.joblib`);

        execFile('python', [model_loaderPath, modelFilePath, document.fileName], (error: any, stdout: any, stderr: any) => {
            console.log(`Executing Python script for ${modelName} model...`);
            console.log(`stdout: ${stdout}`);
            console.log(`stderr: ${stderr}`);

            if (error) {
                console.error(`Error executing Python script for ${modelName} model: ${error}`);
                return;
            }

            // 解析 Python 脚本输出的结果并将其转换为浮点数
            const completionPercentage = parseFloat(stdout.trim());
            console.log(`Completion for ${modelName} model: ${completionPercentage}%`);

            // 将预测结果添加到数组中
            predictions.push(completionPercentage);

            // 如果已经处理了所有模型，则计算中位数并打印
            if (predictions.length === models.length) {
                medianCompletion = calculateMedian(predictions);
                console.log(`Median completion: ${medianCompletion}%`);
                // 保留两位小数
                medianCompletion = Math.round(medianCompletion * 100) / 100;
                const progressBar = generateProgressBar(completionPercentage);
                console.log(`Progress: ${progressBar}`);
                vscode.window.setStatusBarMessage(`Progress: ${progressBar}`, 5000);
            }
    });
}}

function renderProgressBar(percentage: number): string {
    const completed = Math.floor(percentage / 10);
    const remaining = 10 - completed;
    return '*'.repeat(completed) + '_'.repeat(remaining);
}


export function activate(context: vscode.ExtensionContext) {
    console.log(
        'Congratulations, your extension "coding-time-tracker" is now active!'
    );
    codetime = new CodeTime();
    codetime.initialize();
    // codetime.myFunc();
    codetime.getCodeInfo();
    var tiredness = setInterval(codetime.myFunc, 1000 * 20);
    // console.log('Tiredness is: ' + tiredness);

    let userDate = codetime.getToday();
    let userName = codetime.getUserName();
    console.log("!!!!! Log in as " + userName);

    vscode.workspace.onDidChangeTextDocument((event) => {
        console.log("onDidChangeTextDocument");
        if (
            event.document.languageId === "python" &&
            event.document === vscode.window.activeTextEditor?.document
        ) {
            const position = vscode.window.activeTextEditor.selection.start;
            updateStatusBarWithFunctionNames(event.document, position);
        }
    });

    // track cursor position changes
    vscode.window.onDidChangeTextEditorSelection((event) => {
        console.log("onDidChangeTextEditorSelection");
        if (event.textEditor.document.languageId === "python") {
            const position = event.selections[0].start;
            updateStatusBarWithFunctionNames(event.textEditor.document, position);
        }
    });

    console.log('Extension "coding-time-tracker" is now active!');

    if (vscode.workspace.workspaceFolders) {
        let logUri = vscode.Uri.file(
            "/tmp/CodeTime/" + userDate + "/" + userName + "/codeLog"
        );
        console.log("Store data in: " + logUri);

        let userFeedback = vscode.Uri.file(
            "/tmp/CodeTime/" + userDate + "/" + userName + "/feedLog"
        );
        console.log("Store feedback in: " + userFeedback);

        readFile(userFeedback).then((userData) => { }); // readFile(userFeedback)

        readFile(logUri).then((logData) => {
            // let lastActiveEditor: vscode.TextEditor | undefined = undefined;
            vscode.window.onDidChangeActiveTextEditor((activeEditor) => {
                if (activeEditor) {
                    const document = activeEditor.document;
                    // lastActiveEditor = activeEditor;

                    let curTime = new Date().toLocaleTimeString([], {
                        year: "numeric",
                        month: "numeric",
                        day: "numeric",
                        hour: "2-digit",
                        minute: "2-digit",
                    });

                    let lineNum = document.lineCount;

                    logData +=
                        "\n Open: " +
                        curTime.toString() +
                        ", " +
                        document.fileName +
                        ", " +
                        lineNum.toString() +
                        " lines of codes";
                    console.log("Writen in codeLog");
                    vscode.workspace.fs.writeFile(
                        vscode.Uri.file(logUri.path),
                        new TextEncoder().encode(logData)
                    );

                    setTimeout(() => {
                        let curLineNum = document.lineCount;
                        if (curLineNum - lineNum == 0) {
                            // vscode.window.showInformationMessage('Not editing in 1 minute');
                            logData += "\n Not editing in 20 minute";
                            vscode.workspace.fs.writeFile(
                                vscode.Uri.file(logUri.path),
                                new TextEncoder().encode(logData)
                            );
                        }
                    }, 1200000);
                }
            });

            // console.time()
            vscode.workspace.onDidSaveTextDocument((document) => {
                var startTime = performance.now();
                let curTime = new Date().toLocaleTimeString([], {
                    year: "numeric",
                    month: "numeric",
                    day: "numeric",
                    hour: "2-digit",
                    minute: "2-digit",
                });
                // let lineNum = document.lineCount;
                // let content = document.getText();

                // logData += '\n Save: ' + curTime + ', ' + document.fileName + ', ' + lineNum.toString() + ' lines of codes';

                // logData += '\n' + content;
                // vscode.workspace.fs.writeFile(vscode.Uri.file(logUri.path), new TextEncoder().encode(logData));
                var endTime = performance.now();
                console.log(
                    `Call to doSomething took ${endTime - startTime} milliseconds`
                );
            });
            // console.timeEnd()
        });

        let terminalUri = vscode.Uri.file(
            "/tmp/CodeTime/" + userDate + "/" + userName + "/terLog"
        );
        readFile(terminalUri).then((terminalData) => {
            function checkActiveTerminal() {
                let { activeTerminal } = vscode.window;
                // vscode.window.showInformationMessage('avtiveTerminal: ' + (activeTerminal ? activeTerminal.name : '<none>'));
                let curTime = new Date().toLocaleTimeString([], {
                    year: "numeric",
                    month: "numeric",
                    day: "numeric",
                    hour: "2-digit",
                    minute: "2-digit",
                });
                // logData += '\n' + curTime.toString() + ": [Terminal Active] " + activeTerminal?.name
                terminalData += "\n \n" + curTime.toString() + ": [Terminal Active] \n";
                vscode.workspace.fs.writeFile(
                    vscode.Uri.file(terminalUri.path),
                    new TextEncoder().encode(terminalData)
                );
                activeTerminal?.sendText(
                    "script -a " +
                    "/tmp/CodeTime/" +
                    userDate +
                    "/" +
                    userName +
                    "/terLog",
                    true
                );
            }

            checkActiveTerminal();
            vscode.window.onDidChangeActiveTerminal(checkActiveTerminal);

            vscode.window.onDidCloseTerminal((terminal) => {
                let curTime = new Date().toLocaleTimeString([], {
                    year: "numeric",
                    month: "numeric",
                    day: "numeric",
                    hour: "2-digit",
                    minute: "2-digit",
                });
                terminal?.sendText("exit", true);
                terminalData += "\n" + curTime.toString() + ": [Terminal Close] ";
                vscode.workspace.fs.writeFile(
                    vscode.Uri.file(terminalUri.path),
                    new TextEncoder().encode(terminalData)
                );
                // console.log('close terminal');
            });
        }); // readFile(terminalUri)

        // automatically check assignment progress
        // vscode.window.withProgress(
        //     { location: vscode.ProgressLocation.Window, title: "Assignment 1" },
        //     (p) => {
        //         vscode.window.showInformationMessage(
        //             "Estimating your assignment progress..."
        //         );
        //         return new Promise((resolve, reject) => {
        //             p.report({ message: "Start working..." });
        //             let count = 0;
        //             let handle = setInterval(() => {
        //                 count++;
        //                 p.report({ message: "Done " + count + "%" });
        //                 if (count >= 100) {
        //                     clearInterval(handle);
        //                     resolve(1);
        //                     vscode.window.showInformationMessage("Assignment completed!");
        //                 }
        //             }, 500);
        //         });
        //     }
        // );
    }

    // let disposable = vscode.commands.registerCommand(
    //     "coding-time-tracker.check",
    //     () => {
    //         vscode.window.showInformationMessage(
    //             "Estimating the assignment progress..."
    //         );
    //         vscode.window.withProgress(
    //             { location: vscode.ProgressLocation.Window, title: "Assignment 10" },
    //             (p) => {
    //                 return new Promise((resolve, reject) => {
    //                     p.report({ message: "Start working..." });
    //                     let count = 0;
    //                     let handle = setInterval(() => {
    //                         count++;
    //                         p.report({ message: "Done " + count * 10 + "%" });
    //                         if (count >= 10) {
    //                             clearInterval(handle);
    //                             resolve(1);
    //                         }
    //                     }, 1000);
    //                 });
    //             }
    //         );
    //     }
    // );

    // context.subscriptions.push(disposable);
}

export function deactivate() {
    codetime.dispose();
}
