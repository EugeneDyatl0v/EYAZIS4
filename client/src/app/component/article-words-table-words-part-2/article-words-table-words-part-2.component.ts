import {Component, Input, OnInit} from '@angular/core';
import {Word} from "../../model/Word";
import {
    MatCell,
    MatCellDef,
    MatColumnDef,
    MatHeaderCell, MatHeaderCellDef,
    MatHeaderRow,
    MatHeaderRowDef,
    MatRow,
    MatRowDef,
    MatTable
} from "@angular/material/table";

@Component({
    selector: 'app-article-words-table-words-part-2',
    imports: [
        MatCell,
        MatCellDef,
        MatColumnDef,
        MatHeaderCell,
        MatHeaderRow,
        MatHeaderRowDef,
        MatRow,
        MatRowDef,
        MatTable,
        MatHeaderCellDef
    ],
    templateUrl: './article-words-table-words-part-2.component.html',
    standalone: true,
    styleUrl: './article-words-table-words-part-2.component.css'
})
export class ArticleWordsTableWordsPart2Component implements OnInit{
    @Input() data!: any;
    dataSource!: Word[];
    displayedColumns: string[] = ['word', 'part_of_the_speech_tag', "part_of_the_speech_meaning"];

    ngOnInit(): void {
    }

    convertTag(partOfTheSpeechTag: string): string {
        return ""
    }
}
