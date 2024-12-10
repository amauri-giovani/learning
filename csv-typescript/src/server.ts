import express from 'express';
import csvParse from 'csv-parse';
import fs from 'fs';
import path from 'path';

const app = express();

const csvFilePath = path.resolve(__dirname, '../csvFiles/import_template.csv');

const readCSVStream = fs.createReadStream(csvFilePath);
// console.log(readCSVStream);



const parseStream = csvParse({ 
  from_line: 2,
  ltrim: true,
  rtrim: true,
});

const parseCSV = readCSVStream.pipe(parseStream);
// console.log(parseCSV);

parseCSV.on('data', line => {
  // console.log(line);
  const [title, type, value, category] = line;
  console.log(title);
});

parseCSV.on('end', () => {
  console.log('Leitura do CSV finalizada');
});





app.listen(3333, () => {
  console.log('Server started on port 3333');
});