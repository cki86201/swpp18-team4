import { ArbeitRegionEnum } from './Enums/ArbeitRegionEnum';
import { ArbeitTypeEnum } from './Enums/ArbeitTypeEnum';
import { ArbeitPost } from './Classes/ArbeitPost';

export const mockArbeitPost: ArbeitPost[] = [
  { id: 1,
    author_id: 1,
    title: 'mock title 1',
    content: 'mock content 1 A',
    region: ArbeitRegionEnum.SNUStation,
    arbeit_type: ArbeitTypeEnum.Cafe,
    pay: 9000,
    time_zone: ['10:00-15:00'],
    manager_name: '메니저이름',
    manager_phone: '010-1234-1234',
    register_date: new Date(2018, 10, 27),
    edit_date: Date.prototype,
    star: 1.2
  },


  { id: 2,
    author_id: 1,
    title: 'mock title 2',
    content: 'mock content 2 B',
    region: ArbeitRegionEnum.Extra,
    arbeit_type: ArbeitTypeEnum.IT,
    pay: 50000,
    time_zone: ['10:00-15:00'],
    manager_name: '메니저이름',
    manager_phone: '010-1234-1234',
    register_date: new Date(2018, 7, 9),
    edit_date: Date.prototype,
    star: 10
  },
  { id: 3,
    author_id: 1,
    title: 'mock title 3',
    content: 'mock content 3 C',
    region: ArbeitRegionEnum.Nokdu,
    arbeit_type: ArbeitTypeEnum.Design,
    pay: 7500,
    time_zone: ['10:00-15:00'],
    manager_name: '메니저이름',
    manager_phone: '010-1234-1234',
    register_date: new Date(2018, 11, 9),
    edit_date: Date.prototype,
    star: 3.2
  },

  { id: 4,
    author_id: 1,
    title: 'mock title 4',
    content: 'mock content 4',
    region: ArbeitRegionEnum.Nakdae,
    arbeit_type: ArbeitTypeEnum.Tutoring,
    pay: 40000,
    time_zone: ['10:00-15:00'],
    manager_name: '메니저이름',
    manager_phone: '010-1234-1234',
    register_date: new Date(2018, 10, 18),
    edit_date: Date.prototype,
    star: 7.3
  }
];