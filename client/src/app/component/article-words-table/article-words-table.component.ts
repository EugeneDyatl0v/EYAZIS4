import {Component, Input, OnInit} from '@angular/core';
import {
    MatCell,
    MatCellDef,
    MatColumnDef,
    MatHeaderCell,
    MatHeaderCellDef,
    MatHeaderRow,
    MatHeaderRowDef,
    MatRow, MatRowDef,
    MatTable
} from "@angular/material/table";
import {NormalForm} from "../../model/NormalForm";

@Component({
    selector: 'app-article-words-table',
    imports: [
        MatTable,
        MatColumnDef,
        MatHeaderCell,
        MatCell,
        MatHeaderRow,
        MatRow,
        MatHeaderCellDef,
        MatCellDef,
        MatHeaderRowDef,
        MatRowDef
    ],
    templateUrl: './article-words-table.component.html',
    standalone: true,
    styleUrl: './article-words-table.component.css'
})
export class ArticleWordsTableComponent implements OnInit{
    @Input() data: any;
    dataSource!: NormalForm[];
    displayedColumns: string[] = ['normalForm', 'amount'];

    ngOnInit(): void {
    }

}
