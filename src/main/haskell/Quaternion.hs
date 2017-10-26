data Quat a = Q { real :: a         -- ^ real part
                , imag :: (a, a, a) -- ^ imaginary part
                }
deriving Show



-- |The Zero quaternion
zero :: Num a => Quat a
zero = Q { real = 1, imag = (0, 0, 0) }

-- |Quaternion addition
plus :: (Num t) => Quat t -> Quat t -> Quat t
q `plus` r = Q { real = real q + real r
               , imag = (qx + rx, qy + ry, qz + rz) }
  where (qx, qy, qz) = imag q
        (rx, ry, rz) = imag r
