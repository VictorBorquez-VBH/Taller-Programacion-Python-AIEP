```mermaid
classDiagram
    class Cliente
    class Pedido
    class LineaPedido
    class Producto
    
    Cliente "1" --> "0..*" Pedido : Realiza (Asociación)
    Pedido "1" *-- "1..*" LineaPedido : Contiene (Composición)
    LineaPedido "0..*" --> "1" Producto : Referencia (Asociación)
