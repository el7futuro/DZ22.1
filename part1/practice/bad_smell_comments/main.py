# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:

    def move(self, field, x_move, y_move, direction, is_fly, slink,  speed=1):
 
        global new_x, new_y
        if is_fly and slink:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_move + speed
                new_x = x_move
            elif direction == 'DOWN':
                new_y = y_move - speed
                new_x = x_move
            elif direction == 'LEFT':
                new_y = y_move
                new_x = x_move - speed
            elif direction == 'RIGHT':
                new_y = y_move
                new_x = x_move + speed        
                
        if slink:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_move + speed
                new_x = x_move
            elif direction == 'DOWN':
                new_y = y_move - speed
                new_x = x_move
            elif direction == 'LEFT':
                new_y = y_move
                new_x = x_move - speed
            elif direction == 'RIGHT':
                new_y = y_move
                new_x = x_move + speed

            field.set_unit(x=new_x, y=new_y, unit=self)
